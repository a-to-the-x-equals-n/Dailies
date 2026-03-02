// ============================================================
// CHALLENGE: FizzBuzz with Pattern Matching
// Difficulty: Beginner
// Teacher: Ferris
// ============================================================
//
// Welcome back, Rustacean! Ferris here again. Last time you
// conquered vectors and loops - excellent work! Today we're
// going to level up with one of Rust's superpowers: `match`.
//
// Let the compiler guide you to correctness!
//
// DESCRIPTION:
// Implement FizzBuzz for numbers 1 through 20 using a `match`
// expression. For each number, print:
//   - "Fizz"      if divisible by 3 (but not 5)
//   - "Buzz"      if divisible by 5 (but not 3)
//   - "FizzBuzz"  if divisible by both 3 and 5
//   - The number  otherwise
//
// REQUIREMENTS:
// - Use a `for` loop over the range `1..=20`
// - Use a `match` expression to decide what to print
// - Match on the tuple `(n % 3, n % 5)` to keep it clean
//
// EXPECTED OUTPUT:
//     1
//     2
//     Fizz
//     4
//     Buzz
//     Fizz
//     7
//     8
//     Fizz
//     Buzz
//     11
//     Fizz
//     13
//     14
//     FizzBuzz
//     16
//     17
//     Fizz
//     19
//     Buzz
//
// HINTS:
// 1. `match` works on tuples! Try: match (n % 3, n % 5) { ... }
// 2. Each arm of the match uses `=>` to point to the result
// 3. Use `_` as a wildcard to match "anything else"
// 4. Remember: the order of match arms matters - Rust picks
//    the first one that matches!
//
// ============================================================

fn main() {
    // Your code here
}
