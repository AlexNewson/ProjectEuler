defmodule Euler do
  @moduledoc """
  This module fetches solutions for a given problem.
  """

  @doc """
  Solve a Project Euler problem *n* and return the result.
  """

  def solveProblem(n) do
   answer = Module.concat(Solver, "Problem#{n}").solve
   IO.puts("Answer: " <> "#{answer}")
  end
end
