# Contributing to keypress

We’re excited that you want to contribute to **keypress**! Whether it’s a bug fix, new feature, or improvement, your contributions help make this project better.

## How to Contribute

### 1. Fork the Repository

Start by forking the repository on GitHub. This will create a personal copy of the project under your GitHub account where you can make changes.

### 2. Clone Your Fork

Clone your fork to your local machine:

```bash
git clone https://github.com/your-username/keypress.git
```

### 3. Set Up Your Environment

Navigate to the project directory and install dependencies using Poetry:

```bash
cd keypress
poetry install
pre-commit install
```

### 4. Make Your Changes

Create a new branch for your changes:

```bash
git checkout -b your-branch-name
```

Make your changes and commit them with a clear message:

```bash
git add .
git commit -m "Brief description of your changes"
```

### 5. Run Tests

Before submitting a pull request, ensure that all tests pass:

```bash
poetry run pytest
```

### 6. Lint Your Code

Ensure your code adheres to the project’s style guidelines by running:

```bash
poetry run ruff check .
```

### 7. Push Your Changes

Push your changes to your fork:

```bash
git push origin your-branch-name
```

### 8. Create a Pull Request

Go to the repository on GitHub and create a pull request from your branch. Provide a detailed description of your changes and why they’re needed.

## Development Dependencies

The project uses the following development dependencies managed by Poetry:

- **pre-commit**: For managing pre-commit hooks.
- **ruff**: For linting and formatting.
- **pytest**: For testing.

## Questions?

If you have any questions or need further clarification, feel free to open an issue on GitHub or contact us at [rajesh@hyperoot.dev](mailto:rajesh@hyperoot.dev).

Thank you for contributing to **keypress**!
