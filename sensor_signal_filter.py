import numpy as np
from scipy.signal import butter, filtfilt

import matplotlib.pyplot as plt

# --- PROJECT: BIOMEDICAL/INDUSTRIAL SIGNAL FILTERING ---
# Goal: To demonstrate the ability to clean "noisy" sensor data 
# using digital signal processing (DSP) techniques.

def create_noisy_signal():
    """Simulates a sensor reading with background electrical noise."""
    t = np.linspace(0, 1.0, 500)
    # A clean 5Hz sine wave (representing a pulse or a tool vibration)
    clean_signal = np.sin(2 * np.pi * 5 * t)
    # Random high-frequency noise
    noise = 0.5 * np.random.normal(size=t.shape)
    return t, clean_signal + noise, clean_signal

def butter_lowpass_filter(data, cutoff, fs, order=5):
    """Applies a Butterworth Lowpass Filter."""
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

def run_demonstration():
    # Parameters
    fs = 500.0       # Sample rate, Hz
    cutoff = 10.0    # Desired cutoff frequency, Hz
    
    # Generate data
    t, noisy_signal, clean_signal = create_noisy_signal()
    
    # Apply Filter
    filtered_signal = butter_lowpass_filter(noisy_signal, cutoff, fs)
    
    # Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(t, noisy_signal, color='lightgray', label='Raw Noisy Sensor Data')
    plt.plot(t, clean_signal, 'g-', linewidth=2, label='True Signal (Ground Truth)')
    plt.plot(t, filtered_signal, 'r-', linewidth=2, label='Filtered Output (Cleaned)')
    plt.title("SLB Tech Project: Real-time Sensor Noise Reduction")
    plt.xlabel("Time [sec]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    
    # Save the output to show on LinkedIn/Portfolio
    plt.savefig('signal_processing_result.png')
    print("Project executed successfully. Result saved as 'signal_processing_result.png'.")
    plt.show()

if __name__ == "__main__":
    run_demonstration()