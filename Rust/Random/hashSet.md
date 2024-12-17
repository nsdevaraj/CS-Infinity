


```rust
	use std::collections::HashSet;
    fn ans_func(nums: Vec<i32>) -> usize {
        let longest: usize = 0;
        // println!("{:?}", nums);
        // println!("{:?}", nums.into_iter());

        let nums_set: HashSet<i32> = nums.into_iter().collect();

        println!("{:?}", nums_set);
        // println!("{:?}", nums);

        return 0;
    }
```