object Main {
  var threshold = scala.io.StdIn.readInt()

  var summation = for (x <- 1 to threshold if x % 3 == 0 | x % 5 == 0) yield x

  print(summation)
}
