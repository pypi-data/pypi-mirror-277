# locaspy

`locaspy` is a Python package for fetching location, weather, and Google Maps link based on an IP address.

## Installation

To install the package, use the following command:

```bash
pip install locaspy
```

## Usage

### Get Google Maps Link

To get the Google Maps link for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
map_link = locaspy.get_data(ip_address, "map")
print(map_link)
```

### Get Weather Information

To get the weather information for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
weather_info = locaspy.get_data(ip_address, "weather")
print(weather_info)
```

### Get Location Details

To get detailed location information for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
location_info = locaspy.get_data(ip_address, "location")
print(location_info)
```

### Get ISP Information

To get the ISP information for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
isp_info = locaspy.get_data(ip_address, "isp")
print(isp_info)
```

### Get ASN Information

To get the ASN information for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
asn_info = locaspy.get_data(ip_address, "asn")
print(asn_info)
```

### Get Postal Code

To get the postal code for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
postal_code = locaspy.get_data(ip_address, "postal")
print(postal_code)
```

### Get Continent

To get the continent for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
continent = locaspy.get_data(ip_address, "continent")
print(continent)
```

### Get Currency

To get the currency for a given IP address:

```python
import locaspy

ip_address = input("Enter your IP: ")
currency = locaspy.get_data(ip_address, "currency")
print(currency)
```

### Get Languages

To get the languages spoken in the location of a given IP address:

``python
import locaspy

ip_address = input("Enter your IP: ")
languages = locaspy.get_data(ip_address, "languages")
print(languages)
```
