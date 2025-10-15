import inspect
from datetime import date
from pathlib import Path

def auto_doc(heading_template=None):
    """
    Decorator that preserves the original function docstring and
    appends auto-generated Sphinx-style parameter and return type info.
    Optionally adds a heading template at the top.
    """
    def decorator(func):
        sig = inspect.signature(func)
        orig_doc = func.__doc__ or ""
        lines = []

        # Optional heading template
        if heading_template:
            VERSION = Path(__file__).parent.parent.name.split('-')[-1]
            lines.append(heading_template.format(
                name=func.__name__,
                version=VERSION,
                date=date.today().isoformat()
            ))
            lines.append("")  # blank line

        # Include original docstring
        if orig_doc.strip():
            lines.append(orig_doc.strip())
            lines.append("")  # blank line

        # Auto-generate parameters
        if sig.parameters:
            lines.append("Parameters")
            lines.append("----------")
            for name, param in sig.parameters.items():
                annot = param.annotation if param.annotation != inspect.Parameter.empty else "Any"
                default = f", default={param.default}" if param.default != inspect.Parameter.empty else ""
                lines.append(f":param {name}:")
                lines.append(f":type {name}: {annot}{default}")
            lines.append("")

        # Auto-generate return type
        return_annot = sig.return_annotation if sig.return_annotation != inspect.Signature.empty else "Any"
        lines.append(":return:")
        lines.append(f":rtype: {return_annot}")

        func.__doc__ = "\n".join(lines)
        return func
    return decorator

@auto_doc("Function: {name} (module version {version}, generated {date})")
def add(a: int, b: int = 0) -> int:
    """Add two numbers together in a friendly way."""
    return a + b

@auto_doc()
def greet(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

if __name__ == '__main__':
    print(add.__doc__)
    print("\n" + "-"*40 + "\n")
    print(greet.__doc__)
