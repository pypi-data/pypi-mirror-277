# Finding the first, second, and third moments of velocity
This package can be used to calculate moments of velocity in accordance with [Briquet and Aerts (2002)](https://www.aanda.org/articles/aa/pdf/2003/05/aa3122.pdf).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install movel.

```bash
pip install movel
```

## Usage

```python
import movel

# calculates all multi modes for <v>, <v^2>, <v^3>
movel.multi_mode(t, omega, psi, A, B, sigma, vrot)
```

## Contributing

Pull requests are welcome.

## License
[3-Clause BSD](https://opensource.org/license/BSD-3-Clause)
