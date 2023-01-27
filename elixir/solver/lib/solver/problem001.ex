defmodule Solver.Problem1 do

  @moduledoc """
  # [Multiples of 3 and 5](https://projecteuler.net/problem=1)

  If we list all the natural numbers below 10 that are multiples of 3 or 5,
  we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
  the multiples of 3 or 5 below 1000.
  """

  def solve do
    Enum.sum(
      for n <- 1..999,
      Math.multiple?(n, 3) or Math.multiple?(n, 5),
      do: n
    )
  end

end