"""Run with Python 3; fixture checks, not a model or fidelity evaluation."""
from math import cos, sin, sqrt, pi, exp, isclose
from pathlib import Path
import re


def check():
    root = Path(__file__).resolve().parents[1]
    for required in ("SKILL.md", "references/evidence.md", "evaluations.md"):
        assert (root / required).is_file(), required
    for file in root.rglob("*.md"):
        text = file.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if "://" not in link and not link.startswith("#"):
                assert (file.parent / link.split("#")[0]).is_file(), link
        assert not re.search(r"[A-Za-z]:[\\/]Users[\\/]", text), file
    print("package: required files, relative links and private-path check PASS")

    # T1: Eq. 9.16, with the prescribed initial half-step.
    errors = []
    for n in (16, 32, 64):
        h = 1.6 / n
        x, half_v = 1.0, -h / 2
        for _ in range(n):
            x += h * half_v
            half_v -= h * x
        errors.append(abs(x - cos(1.6)))
    assert errors[2] < errors[1] < errors[0]
    assert errors[2] < 5e-5
    print("T1: staggered convergence PASS; errors", errors)

    m, k, x0, v0 = 2.0, 18.0, 0.3, -0.6
    w = sqrt(k / m)
    for t in (0, pi / 6, 0.7, 2.3):
        x = x0 * cos(w * t) + v0 / w * sin(w * t)
        v = -w * x0 * sin(w * t) + v0 * cos(w * t)
        ddx = -w * w * x
        assert isclose(m * ddx + k * x, 0, abs_tol=1e-12)
        assert isclose((m * v * v + k * x * x) / 2, 1.17)
        assert isclose((m * (2*v)**2 + k * (2*x)**2) / 2, 4*1.17)
        if t == 0:
            assert isclose(x, x0) and isclose(v, v0)
        if t == pi / 6:
            assert isclose(x, -0.2) and isclose(v, -0.9)
    print("T2: initial data, residual, energy and scaling PASS")

    L, C, R = 0.5, 0.02, 0.4
    w0, gamma = sqrt(1 / (L*C)), R / L
    assert w0 == 10 and gamma == 0.8
    assert isclose(sqrt(w0*w0-gamma*gamma/4), sqrt(99.84))
    print("T3: circuit frequencies PASS")

    F0 = 1.2
    a = F0 / (2*m*w)
    for t in (0, 0.2, 1.1, 4):
        x = a*t*sin(w*t)
        v = a*(sin(w*t) + w*t*cos(w*t))
        ddx = a*(2*w*cos(w*t) - w*w*t*sin(w*t))
        assert isclose(m*ddx + k*x, F0*cos(w*t), abs_tol=1e-12)
        if t == 0:
            assert x == 0 and v == 0
    print("T4: exact-resonance initial data and forced residual PASS")

    for g in (1, 6, 8):
        d = complex(g*g-36)**0.5
        for r in ((-g+d)/2, (-g-d)/2):
            assert abs(r*r+g*r+9) < 1e-12
    # At critical damping x=(A+B*t)*exp(-3*t) needs the second solution.
    for t in (0, 0.4, 2):
        A, B = 0.3, 0.7
        x = (A+B*t)*exp(-3*t)
        v = (B-3*(A+B*t))*exp(-3*t)
        ddx = (-6*B+9*(A+B*t))*exp(-3*t)
        assert isclose(ddx+6*v+9*x, 0, abs_tol=1e-12)
    print("T5: characteristic and repeated-root residuals PASS")

    assert isclose(cos(pi/2)**2, 0, abs_tol=1e-12)
    assert isclose(cos(2*pi/2), -1)
    print("T6: real-before-square counterexample PASS")

    peak = sqrt(w0*w0-gamma*gamma/2)
    def denominator(f):
        return (w0*w0-f*f)**2 + gamma*gamma*f*f
    assert abs(2*peak*(2*peak*peak-2*w0*w0+gamma*gamma)) < 1e-10
    assert denominator(peak) < denominator(w0)
    print("T11: displacement-response peak PASS")
    print("All fixture checks PASS. Behavioral tests and fidelity remain unmeasured.")


if __name__ == "__main__":
    check()
