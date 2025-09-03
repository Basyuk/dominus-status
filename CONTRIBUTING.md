# Contributing to Dominus Status Service

Thank you for your interest in contributing to Dominus Status Service! We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue using our [bug report template](https://github.com/Basyuk/dominus-status/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D+).

Please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Docker version, etc.)
- Relevant logs

### Suggesting Features

We love new ideas! Please create a [feature request](https://github.com/Basyuk/dominus-status/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFEATURE%5D+) and describe:
- The problem you're trying to solve
- Your proposed solution
- Use cases and benefits
- Any implementation considerations

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/Basyuk/dominus-status.git
   cd dominus-status
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the service locally**
   ```bash
   uvicorn dominus-status.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Test with Docker**
   ```bash
   docker-compose build
   docker-compose up
   ```

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Comment complex logic
- All comments and documentation should be in English

### Testing

- Test your changes locally before submitting
- Test both authentication modes (local and Keycloak)
- Verify Docker builds and runs correctly
- Test API endpoints with curl or similar tools

### Pull Request Process

1. **Create a branch** for your feature/fix
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Keep commits small and focused
   - Use descriptive commit messages
   - Follow conventional commit format if possible

3. **Update documentation** if needed
   - Update README.md if you add features
   - Add/update docstrings
   - Update API documentation

4. **Test your changes**
   - Run the service locally
   - Test with Docker
   - Verify both auth modes work

5. **Submit a pull request**
   - Use a clear title and description
   - Reference any related issues
   - Describe what you changed and why

### Code Review

- All submissions require review
- We may suggest changes, reasons, or alternatives
- Keep discussions respectful and constructive
- Address feedback promptly

### Commit Message Format

We prefer conventional commit messages:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build process or auxiliary tool changes

Examples:
```
feat(auth): add support for custom JWT claims
fix(docker): resolve container startup race condition
docs(readme): update installation instructions
```

### Getting Help

- Create an issue for questions
- Join discussions on existing issues
- Check existing documentation first

### License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Development Guidelines

### Authentication Development

- Test both local and Keycloak authentication
- Ensure backward compatibility
- Document configuration changes

### Docker Development

- Test multi-container setups
- Verify volume mounts work correctly
- Check environment variable handling

### API Development

- Follow RESTful principles
- Add proper error handling
- Document new endpoints
- Maintain response format consistency

### Security Considerations

- Never commit secrets or passwords
- Use environment variables for sensitive data
- Follow security best practices
- Report security issues privately

Thank you for contributing! 🎉
