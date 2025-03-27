# POC-APIs-security


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/guillaumepot/POC-APIs-security">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">POC - OWASP 2023 - Top 10 API vulnerabilities</h3>

  <p align="center">
    POC - OWASP top 10 API vulnerabilities - 2023
    <br />
    <a href="https://github.com/guillaumepot/POC-APIs-security"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/guillaumepot/POC-APIs-security/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/guillaumepot/POC-APIs-security/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://owasp.org/API-Security/editions/2023/en/images/cover.jpg)
Secure your APIs, OWASP top 10 API vulnerabilities - 2023

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]](https://www.python.org/)
* [![FastAPI][FastAPI]](https://fastapi.tiangolo.com/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

```
Create uv environment and install the requirements:
- uv sync
```

### Prerequisites

* uv (https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
  ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/guillaumepot/POC-APIs-security.git
   ```
2. Setup venv
   ```sh
   uv sync
   ```
3. Generate .env in ./src/config, add the following content
   ```sh
    DB_NAME='./database/example_database.db'
    API_HOST='localhost'
    API_PORT=8000
   ```
4. [Optional] You can (re)generate the mock database 'database.db' and the test_api logs
   ```sh
  uv run ./scripts/generate_example_database.py
   ```
5. Start server
   ```sh
   uv run main.py
   ```
6. Log in using these account to test
   ```sh
   admin:admin
   John Doe:johndoe
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

[WIP]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] API1:2023 - Broken Object Level Authorization
- [X] API2:2023 - Broken Authentication
- [ ] API3:2023 - Broken Object Property Level Authorization
- [ ] API4:2023 - Unrestricted Resource Consumption
- [ ] API5:2023 - Broken Function Level Authorization
- [ ] API6:2023 - Unrestricted Access to Sensitive Business Flows
- [ ] API7:2023 - Server Side Request Forgery
- [ ] API8:2023 - Security Misconfiguration
- [ ] API9:2023 - Improper Inventory Management
- [ ] API10:2023 - Unsafe Consumption of APIs

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Top contributors:

<a href="https://github.com/guillaumepot/POC-APIs-security/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=guillaumepot/POC-APIs-security" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Guillaume Pot

[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/062guillaumepot/)  
[![Github Badge](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=GitHub%20Pages&logoColor=white)](https://github.com/guillaumepot)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<!-- * []()
* []()
* []() -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[![OWASP 2023 Top10 API vulnerabilities](https://img.shields.io/badge/OWASP-2023_Top10_API_vulnerabilities-blue)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)