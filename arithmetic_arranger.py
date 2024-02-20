def arithmetic_arranger(problems, result=False):

  ############
  # Edge Case
  ############
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ""
  line1 = line2 = line3 = line4 = ""
  operand = ""


  
  ############
  # Split and cleanse the formula
  ############
  for problem in problems:
    if "+" not in problem and "-" not in problem:
      return "Error: Operator must be '+' or '-'."

    if "+" in problem:
      operand = "+"
      problem = problem.split("+")
    if "-" in problem:
      operand = "-"
      problem = problem.split("-")

    problem[0] = problem[0].strip()
    problem[1] = problem[1].strip()
    
    if len(problem[0]) > 4 or len(problem[1]) > 4:
      return "Error: Numbers cannot be more than four digits."
    try:
      num1 = int(problem[0])
      num2 = int(problem[1])
    except:
      return "Error: Numbers must only contain digits."



    ############
    # Formatting and Output
    ############
    length = max(len(problem[0]), len(problem[1]))
    line1 += problem[0].rjust(length+2) + "    "
    line2 += operand + " " + problem[1].rjust(length) + "    "
    line3 += "-"*(length + 2) + "    "

    if result:
      if operand == "+":
        total = num1 + num2
      else:
        total = num1 - num2
      line4 += str(total).rjust(length+2) + "    "

  line1 = line1.rstrip() + "\n"
  line2 = line2.rstrip() + "\n"
  line3 = line3.rstrip()
  arranged_problems = line1 + line2 + line3
  
  if result:
    arranged_problems += "\n" + line4.rstrip()

  return arranged_problems