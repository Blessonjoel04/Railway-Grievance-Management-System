document.addEventListener("DOMContentLoaded", function() {
    // Login button and popup
    const loginBtn = document.getElementById("loginBtn");
    const loginPopup = document.getElementById("loginPopup");
    const loginClose = document.getElementById("loginClose");

    loginBtn.addEventListener("click", function() {
        loginPopup.style.display = "block";
    });

    loginClose.addEventListener("click", function() {
        loginPopup.style.display = "none";
    });

    // Submit login form
    window.submitLogin = function() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        if (username === 'Blesson' && password === 'root') {
            // Redirect to staff page if login is successful
            window.location.href = "/staff";
        } else {
            alert("Invalid username or password");
        }
    };

    // Handle 'Station Issue' button click
    const stationIssueButton = document.querySelector(".sidebar-options a[href='station_issue_grievance.html']");
    if (stationIssueButton) {
        stationIssueButton.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default anchor behavior
            window.location.href = "/station_issue_grievance";
        });
    }

    // Handle OTP button
    window.getOTP = function() {
        alert("OTP has been sent to your mobile number.");
    };

    // Chatbot button and popup
    const chatbotButton = document.getElementById("chatbotButton");
    const chatbotPopup = document.getElementById("chatbotPopup");

    chatbotButton.addEventListener("click", function() {
        chatbotPopup.style.display = chatbotPopup.style.display === "block" ? "none" : "block";
    });

    // Close chatbot popup when clicking outside of the popup
    window.addEventListener("click", function(event) {
        if (event.target === chatbotPopup) {
            chatbotPopup.style.display = "none";
        }
    });
});
