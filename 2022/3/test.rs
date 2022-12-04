use std::collections::HashSet;

fn main() {
    let a: HashSet<u32> = vec![1,2,3,4,5].into_iter().collect();

    a.iter().reduce(|a, b| {
        println!("{:?}, {:?}", a, b);
        return a;
    });
}
