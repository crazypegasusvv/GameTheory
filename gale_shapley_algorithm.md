<!DOCTYPE HTML>
<html>
  <head>
    <h1>Stable Marriage Problem</h1>
  </head>
  <body>
    <p>Finding a stable matching using Gale-Shapley Algorithm</p>
    <p>Read about the Stable Marriage Problem wiki <a href="https://en.wikipedia.org/wiki/Stable_marriage_problem">here.</a></p>
    <p>
      <pre>
        <a href="https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm">Gale-Shapley Algorithm(M, W):</a>
        Initialize all m ∈ M and w ∈ W to free
        while ∃ free man m who still has a woman w to propose to do
            w := first woman on m's list to whom m has not yet proposed
            if w is free then
                (m, w) become engaged
            else some pair (m', w) already exists
                if w prefers m to m' then
                    m' becomes free
                    (m, w) become engaged 
                else
                    (m', w) remain engaged
                end if
            end if
        repeat
      </pre>
     </p>
  </body>
</html>
