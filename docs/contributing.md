# Guidelines for Contributing to QubiPy

We welcome contributions! Here's how you can help make QubiPy better:

!!! info "Ways to Contribute"
   * Submit bug reports and feature requests
   * Improve documentation
   * Write code patches
   * Create or improve tests
   * Review pull requests

### Getting Started

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request


### Guidelines

!!! warning "Before Contributing"
   - Check if an issue already exists for your problem
   - Follow our coding standards and conventions
   - Write meaningful commit messages (we use Conventional Commits)
   - Include tests for new features
   - Update documentation as needed

!!! tip "Quick Links"
    - [Report a Bug](https://github.com/QubiPy-Labs/QubiPy/blob/main/.github/ISSUE_TEMPLATE/bug_report.md)
    - [Request a Feature](https://github.com/QubiPy-Labs/QubiPy/blob/main/.github/ISSUE_TEMPLATE/feature_request.md)
    - [Read the Documentation](https://qubipy.readthedocs.io)

## Code Style

!!! info "Python Style Guide"
    - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
    - Use meaningful variable and function names
    - Keep functions focused and concise
    - Add docstrings to all public methods and classes
    - Maximum line length: 88 characters

### Docstring Format

```python
def example_function(param1: str, param2: int) -> bool:
    """Short description of function.

    Longer description if needed.

    Parameters
    ----------
    param1 : str
        Description of param1
    param2 : int
        Description of param2

    Returns
    -------
    bool
        Description of return value

    Raises
    ------
    ValueError
        When and why this error is raised
    """
    pass
```

## Commit Messages

!!! example "Commit Message Format"
    ```
    <type>(<scope>): <description>

    [optional body]

    [optional footer]
    ```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

### Examples
```bash
feat(rpc): add new transaction broadcast method
fix(core): resolve connection timeout issue
docs: update installation instructions
test: add unit tests for core client
```

!!! tip "Good Commit Messages Should"

- Be clear and concise
- Describe what changes were made and why
- Reference issue numbers when applicable
- Use the imperative mood ("add" not "added")

## Pull Request Process

!!! info "Step by Step"
   1. Fork the repository
   2. Create a feature branch (`git checkout -b feature/amazing-feature`)
   3. Make your changes
   4. Run tests
   5. Update documentation if needed
   6. Commit your changes (following commit message guidelines)
   7. Push to your fork
   8. Create a Pull Request

### Before Submitting

!!! warning "Checklist"
   Make sure:

   - Tests are passing
   - Documentation is updated
   - Code follows style guidelines
   - Commit messages follow guidelines
   - Branch is up to date with main

### Example PR Description Template

```markdown
## Description
Please include a summary of the change and which issue is fixed.

## Type of change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

## Testing

!!! info "Running Tests"
    ```bash
    # Run all tests
    pytest

    # Run specific test file
    pytest tests/test_rpc.py

    # Run with coverage report
    pytest --cov=qubipy tests/
    ```

### Test Guidelines

!!! tip "Writing Tests"
    - Write tests for all new features and bug fixes
    - Use descriptive test names that explain the scenario
    - Include docstrings explaining the test's purpose
    - Mock external API calls
    - Test both success and failure cases

!!! note "Test Structure"
    We use pytest fixtures defined in `conftest.py` for:

    * Mocking API responses
    * Providing sample test data
    * Setting up test clients
    * Common test configurations

!!! warning "Before Pushing"
Make sure to:

- Run the full test suite
- Check test coverage
- Verify no tests are failing

### Need Help?

!!! question "Have Questions?"
   * Browse [existing issues](https://github.com/QubiPy-Labs/QubiPy/issues)
   * Join our [Discord community](https://discord.gg/EejFQdQkhG)
   * Check the [documentation](https://qubipy.readthedocs.io)

### Code of Conduct

Please note that this project adheres to a [Code of Conduct](code_of_conduct.md). By participating in this project, you agree to abide by its terms.