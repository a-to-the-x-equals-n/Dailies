// ============================================================================
// CHALLENGE: Find the Maximum
// Difficulty: Beginner
// ============================================================================
//
// Hey there, fellow Rustacean! Ferris here, ready to help you take your first
// steps into the wonderful world of Rust. Today we'll work with vectors and
// loops - two fundamental tools you'll use constantly.
//
// Let the compiler guide you to correctness!
//
// DESCRIPTION:
// Write a function called `find_max` that takes a vector of integers and
// returns the largest value.
//
// REQUIREMENTS:
// - Create a function `find_max(numbers: Vec<i32>) -> i32`
// - The function should return the largest integer in the vector
// - You may assume the vector is never empty
// - Use a loop to iterate through the vector
//
// EXPECTED OUTPUT:
// The maximum value is: 9
//
// HINTS:
// 1. You'll need a mutable variable to track the current maximum
// 2. Start by assuming the first element is the maximum
// 3. The `for` loop works great with vectors: `for num in &numbers { ... }`
// 4. The compiler is your friend! Read error messages carefully.
//
// ============================================================================

pub fn find_max(n: Vec<i32>) -> i32 {
	let mut x = -1;

	for i in 0..n.len() {
		if x < n[i] {
			x = n[i];
		}
	}

	x
}

fn main() {
	let numbers = vec![3, 7, 2, 9, 4, 1];
	let max = find_max(numbers);
	println!("The maximum value is: {}", max);
}

// ============================================================================
// FEEDBACK FROM FERRIS
// ============================================================================
//
// It compiles and runs correctly - nice work!
//
// WHAT YOU DID WELL:
// - Correct function signature
// - Loop logic is sound
// - Proper use of mutability with `let mut`
//
// ONE BUG TO CONSIDER:
// Initializing `x = -1` works here, but what if all numbers were negative?
//
//     let numbers = vec![-5, -3, -8, -2];  // Should return -2, but you'd get -1
//
// Fix: Initialize with the first element instead:
//
//     let mut x = n[0];
//     for i in 1..n.len() { ... }
//
// IDIOMATIC RUST TIP:
// Your index-based loop works, but Rust prefers direct iteration:
//
//     for &num in &n {
//         if num > x { x = num; }
//     }
//
// This avoids bounds checking overhead and is more readable.
//
// Overall, solid first solution! You got the logic right, which is the hard
// part. The refinements are just Rust style.
//
// "In Rust, we don't fight the borrow checker - we dance with it!" - Ferris
// ============================================================================
