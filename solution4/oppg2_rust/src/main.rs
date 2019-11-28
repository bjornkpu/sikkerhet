
fn main() {
    let s = "Hallo & < > && << >>".to_string();
    println!("{}", s);
    println!("{}", replace_all(s));
}


fn replace_all(string: std::string::String) -> std::string::String{
    let repl_amp = string.replace("&","&amp");
    let repl_lt = repl_amp.replace("<","&lt");
    let repl_gt = repl_lt.replace(">","&gt");
    return repl_gt;    
}