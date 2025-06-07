factorial <- function(n) {
  if (n == 1 || n == 0) {
    return(1)
  } else {
    return(n * factorial(n - 1))
  }
}

num <- as.numeric(readline(prompt = "Number: "))

if (num < 0) {
  print("dne")
} else if (num %% 1 != 0) {
  print("dne")
} else {
  print(factorial(num))
}