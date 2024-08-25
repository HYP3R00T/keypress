<h1 align="center">keypress</h1>

<p align="center">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/HYP3R00T/keypress/publish.yml?style=for-the-badge&labelColor=%2324273a&color=%23b7bdf8">
<a src="https://pypi.org/project/keypress/" target="_blank">
<img alt="Pypi versions" src="https://img.shields.io/pypi/v/keypress?style=for-the-badge&labelColor=%2324273a&color=%23b7bdf8">
</a>
</p>

This module offers a comprehensive solution for handling keyboard input across platforms. Whether you’re detecting simple keypresses or complex key combinations, our `get_key` function and `Keys` constants deliver robust functionality with clear, descriptive outputs. Perfect for developers needing to implement precise keyboard interactions in their applications.

## Installation

You can install **keypress** via [pip](https://pypi.org/project/keypress/):

```bash
pip install keypress
```

## Example

You can run **keypress** in your terminal.

```python
from keypress import Keys, get_key

if __name__ == "__main__":
    key = ""
    while key not in ["q", Keys.ENTER]:
        key = get_key()
        if key.is_printable:
            print(key)
        print(key.key_codes)
        print(key.description)
```

## Contributing

Contributions are welcome! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
