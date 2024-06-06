from latss import LATSS
import pickle
import mne
from mne.io import concatenate_raws, read_raw_edf
from mne.channels import make_standard_montage
from mne.datasets import eegbci
import pytest

def sim_calib_data():
    channels = ["C3", "C4", "P3", "P4", "T7", "T8", "P7", "P8"] # These positions of the 10-10 system are equivalent to our positions in the 10-20 system
    montage = make_standard_montage("standard_1005")

    raws = []

    for subject in range(1, 9):
        
        f_names = eegbci.load_data(subject, runs=[6, 10, 14], path="tests/test_data", update_path=True)
        raw = concatenate_raws([read_raw_edf(f_name, preload=True) for f_name in f_names])

        eegbci.standardize(raw)  # set channel names
        raw.set_montage(montage)
        raw.annotations.rename(dict(T0="other", T1="other", T2="feet"))
        raw.set_eeg_reference()

        raw.drop_channels([ch for ch in raw.ch_names if ch not in channels])

        raws.append(raw)

    return raw

def sim_test_data(model_params: dict):
    channels = ["C3", "C4", "P3", "P4", "T7", "T8", "P7", "P8"] # These positions of the 10-10 system are equivalent to our positions in the 10-20 system
    montage = make_standard_montage("standard_1005")

    f_names = eegbci.load_data(10, runs=[6], path="tests/test_data", update_path=True)
    raw = concatenate_raws([read_raw_edf(f_name, preload=True) for f_name in f_names])

    eegbci.standardize(raw)  # set channel names
    raw.set_montage(montage)
    raw.annotations.rename(dict(T0="other", T1="other", T2="feet"))
    raw.set_eeg_reference()

    raw.drop_channels([ch for ch in raw.ch_names if ch not in channels])

    # drop annotations
    raw.annotations.delete([0, 1, 2])

    length = model_params["epoch_length"] if model_params["window_size"] is None else model_params["window_size"]
    sfreq = model_params["sfreq"]

    if raw.info["sfreq"] != sfreq:
        raw.resample(sfreq)

    # Equivalent to one epoch by model requirements
    raw = raw.crop(tmax=length * 5, include_tmax=False)

    return raw

def test_latss():
    # Load the source data
    with open("tests/test_data/physionet_processed.pkl", "rb") as f:
        source_data = pickle.load(f)
        
    # Initialize the LATSS model
    model = LATSS(source_data=source_data, sfreq=160, epoch_length=3, window_size=1, window_overlap=0.5)

    # Calibrate the model
    raw = sim_calib_data()
    acc = model.calibrate(raw, event_id={"other": 0, "feet": 1})

    # Predict the labels for the test data
    test_raw = sim_test_data(model.get_params())
    pred = model.predict(test_raw)

    print(f"Accuracy: {acc}")
    print(f"Predictions: {pred}")


def main():
    test_latss()

if __name__ == "__main__":
    main()