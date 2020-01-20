# pybluebolt-tcp: Python interface for BlueBOLT over TCP

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=WREP29UDAMB6G)

Python library for directly communicating over TCP with power management devices that have [BlueBOLT](https://www.panamax.com/power-management/bluebolt-20-ip-power-management) support, as opposed to communicating via the BlueBOLT cloud (see pybluebolt for cloud communication).

NOTE:

* This library is community supported, please submit changes and improvements.
* This is a very basic beta-quality interface that may need to be refactored in the future.

## Installation

```
pip3 install pybluebolt-tcp
```

## Examples

```python-tcp
bluebolt = PyBlueboltTCP(host, port)
bluebolt.status

bluebolt.outlets[1].turn_off()
```

See also [example-client.py](example-client.py) for a more comprehensive working example.

## Supported Hardware

Requires CV-1 or CV-2 card installed in:

* [Panamax M4315-Pro 8-outlet](https://www.amazon.com/Panamax-M4315-PRO-Bluebolt-Management-Monitoring/dp/B003XEAQTU?tag=rynoshark-20)
* [Panamax M4320-Pro 8 outlet](https://www.amazon.com/Panamax-M4320-Programmable-Power-Management/dp/B007I4GLQI?tag=rynoshark-20)
* [Panamax M4000 8 outlet](https://www.amazon.com/Panamax-Outlet-BlueBOLT-Programmable-Management/dp/B00WK646I4?tag=rynoshark-20)

## Known Issues


## See Also

* [MyBlueBOLT Portal](https://www.mybluebolt.com/)
* [pybluebolt-service for BlueBOLT cloud support](https://github.com/rsnodgrass/pybluebolt-service)
* [BlueBOLT device proxy web service](https://github.com/Tenflare/bluebolt-api)
* Home Assistant integration for BlueBOLT devices: [hass-bluebolt](https://github.com/rsnodgrass/hass-bluebolt)
