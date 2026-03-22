// Social Reputation System Main JS

document.addEventListener('DOMContentLoaded', () => {
    // Universal Toast Auto-dismiss
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(-10px)';
            setTimeout(() => toast.remove(), 500);
        }, 5000);
    });
});

// Utility for copying to clipboard
function copyToClipboard(text) {
    const input = document.createElement('input');
    input.value = text;
    document.body.appendChild(input);
    input.select();
    document.body.removeChild(input);
}

// Global Auth Utils (used in templates inline for simplicity)
async function sendOTPRequest(phone) {
    try {
        const response = await fetch('/send-otp', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({phone})
        });
        return await response.json();
    } catch (e) {
        console.error("OTP Error:", e);
        return {success: false, message: "Network error"};
    }
}
