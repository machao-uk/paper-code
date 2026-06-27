#!/usr/bin/env julia
# MathZ_interior_certificate.jl
#
# Machine certificate: n=4 reduced Pick matrix PSD on interior non-confluent cells.
#
# Method: interval arithmetic + adaptive subdivision (Gershgorin eigenvalue lower bound).
# Domain: |lambda_j| <= R=0.97. Boundary |lambda_j|->1 handled analytically in TeX
#         (Prop. prop:full-three-plus-one-reduced-pick + Prop. prop:radial-square-model).
#
# Usage:
#   julia -e 'import Pkg; Pkg.add("IntervalArithmetic")' # first time only
#   julia MathZ_interior_certificate.jl
#
# Output: prints "CERTIFICATE COMPLETE" if all boxes certified, else reports problematic box.
# Expected runtime: several hours (leave overnight).

using IntervalArithmetic, Printf, Dates

println("MathZ n=4 Reduced Pick Certificate")
println("Started: ", Dates.format(now(), "yyyy-mm-dd HH:MM:SS"))
println()

# ─────────────────────────────────────────────────────────────────────────────
# Polynomial: c1,c2,c3 from quartic discriminant partials
# Delta(a0,a1,a2) = 256a0^3 - 128a0^2*a2^2 + 144a0*a1^2*a2 + 16a0*a2^4 - 27a1^4 - 4a1^2*a2^3
# c1 = -(Delta_{a2} + a2*Delta_{a0}), c2 = -Delta_{a1}, c3 = -Delta_{a0}
# ─────────────────────────────────────────────────────────────────────────────

function compute_rs(l1, l2, l3, l4)
    e2 = l1*l2+l1*l3+l1*l4+l2*l3+l2*l4+l3*l4
    e3 = l1*l2*l3+l1*l2*l4+l1*l3*l4+l2*l3*l4
    e4 = l1*l2*l3*l4
    a0, a1, a2 = e4, -e3, e2
    c1 = -512*a0^2*a2 - 144*a0*a1^2 + 192*a0*a2^3 - 132*a1^2*a2^2 - 16*a2^5
    c2 = -288*a0*a1*a2 + 108*a1^3 + 8*a1*a2^3
    c3 = -768*a0^2 + 256*a0*a2^2 - 144*a1^2*a2 - 16*a2^4
    return [(c1 + c2*l + c3*l^2) / 768 for l in (l1,l2,l3,l4)]
end

# ─────────────────────────────────────────────────────────────────────────────
# Interval Cholesky PSD check for 4x4 Hermitian reduced Pick matrix.
# Returns true iff all Cholesky pivots certified > 0 (hence matrix is PSD).
# ─────────────────────────────────────────────────────────────────────────────

function pick_matrix_entries(lams, rs)
    # Returns 4x4 array of complex interval entries M[i,j]
    n = 4
    M = Matrix{Complex{Interval{Float64}}}(undef, n, n)
    for i in 1:n, j in 1:n
        ri, rj = rs[i], rs[j]
        li, lj = lams[i], lams[j]
        num = 1 - ri * conj(rj)
        den = 1 - li * conj(lj)
        M[i,j] = num / den
    end
    return M
end

function interval_cholesky_psd(lams, rs)
    # Attempt Cholesky on 4×4 Hermitian Pick matrix.
    # Returns :certified if all 4 pivots > 0, :fail otherwise.
    n = 4
    M = pick_matrix_entries(lams, rs)

    # L is lower triangular (complex interval). We only need diagonal (real) pivots.
    # Work on copy A = M, eliminate in-place (LDL* style with D = pivot^2).
    # Use standard Cholesky: pivot_k = A[k,k] - sum_{j<k} |L[k,j]|^2
    # where L[k,j] = A[k,j] / sqrt(pivot_j)
    # Equivalently (Cholesky-Banachiewicz): track A and zero out columns sequentially.

    A = copy(M)
    for k in 1:n
        # Pivot = real part of A[k,k] (should be real for Hermitian matrix)
        pivot = real(A[k,k])
        inf(pivot) <= 0 && return :fail

        sqp = sqrt(pivot)     # interval sqrt of pivot

        # Update remaining submatrix: A[i,j] -= A[i,k]*conj(A[j,k]) / pivot
        for i in k+1:n
            Aik_over_sqp = A[i,k] / sqp
            for j in k+1:n
                A[i,j] = A[i,j] - Aik_over_sqp * conj(A[j,k] / sqp)
            end
        end
    end
    return :certified
end

# ─────────────────────────────────────────────────────────────────────────────
# Certify one box. Returns :certified, :outside, or :subdivide.
# Box: (x1,x2,y2,x3,y3) with l1=x1 (real), l2=x2+iy2, l3=x3+iy3, l4=-(l1+l2+l3).
# ─────────────────────────────────────────────────────────────────────────────

function certify(x1::T, x2::T, y2::T, x3::T, y3::T) where T <: Interval
    z = zero(x1)
    l1 = complex(x1, z)
    l2 = complex(x2, y2)
    l3 = complex(x3, y3)
    l4 = -(l1 + l2 + l3)

    # Domain constraint: all |lambda_j|^2 in [0, R^2)
    # - inf(a2) >= R^2: box entirely in annulus R<=|λ|<1, covered by blow-up lemma
    # - inf(a2) >= 1.0: box entirely outside unit disk
    # - sup(a2) > 1.0: box straddles unit circle → subdivide
    for l in (l1, l2, l3, l4)
        a2 = real(l)^2 + imag(l)^2
        inf(a2) >= R*R  && return :outside    # annulus covered analytically
        sup(a2) > 1.0   && return :subdivide  # straddles unit circle, bisect
    end

    rs = compute_rs(l1, l2, l3, l4)

    # Interval Cholesky: certified iff all 4 pivots strictly positive
    result = interval_cholesky_psd((l1,l2,l3,l4), rs)
    result == :certified && return :certified
    return :subdivide
end

# ─────────────────────────────────────────────────────────────────────────────
# Adaptive subdivision
# ─────────────────────────────────────────────────────────────────────────────

const Box = NTuple{5, Interval{Float64}}

function bisect(b::Box)
    ws = diam.(b)
    k  = argmax(ws)
    m  = mid(b[k])

    lo = ntuple(i -> i == k ? intersect_interval(b[i], interval(-Inf, m)) : b[i], 5)
    hi = ntuple(i -> i == k ? intersect_interval(b[i], interval(m, Inf))  : b[i], 5)
    return lo, hi
end

# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

const R = 0.97          # truncation radius
const LOG_INTERVAL = 100_000   # print progress every N steps
const MAX_QUEUE    = 20_000_000 # safety cap

init_box::Box = (
    interval(0.0, R),    # x1 = Re(l1), fixed real by rotation
    interval(-R, R),     # x2 = Re(l2)
    interval(-R, R),     # y2 = Im(l2)
    interval(-R, R),     # x3 = Re(l3)
    interval(-R, R),     # y3 = Im(l3)
)

queue    = Box[init_box]
n_cert   = 0
n_out    = 0
n_steps  = 0
n_fail   = 0
fail_box = nothing
t0       = time()

println("Domain: x1∈[0,$R], (x2,y2)∈[-$R,$R]², (x3,y3)∈[-$R,$R]²")
println("Boundary |λ_j|>$R handled by blow-up lemma in TeX.\n")

while !isempty(queue)
    length(queue) > MAX_QUEUE && (println("⚠ Queue cap reached. Increase MAX_QUEUE."); break)

    b  = pop!(queue)
    st = certify(b...)
    global n_steps += 1

    if st == :certified
        global n_cert += 1
    elseif st == :outside
        global n_out += 1
    else
        if maximum(diam.(b)) < 1e-8
            global n_fail += 1
            global fail_box = b
            msg = @sprintf("  ✗ Failed tiny box: x1=%s x2=%s y2=%s x3=%s y3=%s\n", string.(b)...)
            print(msg)
            open("/tmp/pick_fails.txt", "a") do f; write(f, msg); end
        else
            lo, hi = bisect(b)
            push!(queue, lo)
            push!(queue, hi)
        end
    end

    if n_steps % LOG_INTERVAL == 0
        @printf("[%s] steps=%8d  cert=%8d  out=%8d  queue=%8d  fail=%d\n",
                Dates.format(now(),"HH:MM:SS"),
                n_steps, n_cert, n_out, length(queue), n_fail)
        flush(stdout)
    end
end

println()
println("="^65)
if isempty(queue) && n_fail == 0
    println("✓  CERTIFICATE COMPLETE")
    println()
    println("The 4×4 reduced Pick matrix Π^red_λ is positive semidefinite")
    println("for every centred interior non-confluent quadruple with |λ_j| ≤ $R.")
    println("Combined with Prop. prop:full-three-plus-one-reduced-pick and")
    println("Prop. prop:radial-square-model, Conjecture 3.4 holds globally.")
elseif n_fail > 0
    println("✗  CERTIFICATE INCOMPLETE: $n_fail boxes not certified.")
    println("   Consider tighter eigenvalue bounds (IntervalLinearAlgebra.jl).")
else
    println("⚠  Queue cap reached: certificate incomplete.")
end
println()
@printf("Certified boxes : %d\n", n_cert)
@printf("Outside domain  : %d\n", n_out)
@printf("Failed boxes    : %d\n", n_fail)
@printf("Total steps     : %d\n", n_steps)
@printf("Total time      : %.0f s (%.1f min)\n", time()-t0, (time()-t0)/60)
println("="^65)
