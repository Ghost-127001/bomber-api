# OTP/Email/Call **Bomber API** Collection 

### 📖 About
A collection of Endpoint APIs specifically used for triggering OTP requests.
Extracted from live websites.


### ✨ Features
Contains structured dictionaries for SMs/Call/Email endpoints APIs.
Demonstrates complex header management, session tokens, and payload formatting.

### 🚀 Usage Instructions
APIs use a lambda function in the `data` field to format the payload dynamically.
You **MUST** pass an actual phone number (or user input) to generate the request body.

Example API Configuration:
```python
{
    "url": "[https://api.example.com/send-otp](https://api.example.com/send-otp)",
    "method": "POST",
    "headers": {
        "accept": "application/json",
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0..."
    },
    "data": lambda phone: json.dumps({"phone_number": phone}),
    "count": 10
}
```
> [!NOTE]
> **Maintenance & Contributions:** Currently, **98% of the APIs are working perfectly**. Some may expire as they are temporary, but the API file is updated . 
> Forks and Pull Requests are highly encouraged! If you find this project useful, please consider giving it a ⭐ **Star**!

### 📂 Version History

| Version | Status | Description | Link |
| :--- | :--- | :--- | :--- |
| **v3.0** | **Coming Soon** | .... |
| **v2.0** | **Latest** | Added more Endpoint APIs | [ **API_2**](https://drive.google.com/uc?export=download&id=1CpssaxcWm1atPrmQDZ1_lrDzrTz9EXWS) |
| **v1.0** | Legacy | Original collection | [ **API_1**](./api_config.py) |


### ⚠️ Disclaimer
This repository is strictly for educational research and security testing only.
Do not use this API's for SMS/Call/Email bombing, spamming, or any malicious activities.

<div align="center">
  
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/YOUR_USERNAME)
  
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ghostt.in)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ghostt_ttt)
[![Website](https://img.shields.io/badge/Personal%20Website-000000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://YOUR_WEBSITE.com)

</div>
<div align="center">

`Owner-@pkmn.abhi`
`Made with 🤎`

</div>
