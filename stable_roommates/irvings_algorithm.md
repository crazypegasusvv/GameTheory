<!DOCTYPE HTML>
<html>
  <head>
    <h1>Stable Roommates Problem</h1>
  </head>
  <body>
    <p>Finding a stable pairs of roommates using Irving's Algorithm</p>
    <p>Read about the Stable Roommate Problem wiki <a href="https://en.wikipedia.org/wiki/Stable_roommates_problem">here.</a></p>
    <p>
      <pre>
        <a href="http://www.dcs.gla.ac.uk/~pat/jchoco/roommates/papers/Comp_sdarticle.pdf">Irving's Algorithm:</a>
        &nbsp;
        <i><b>Phase one:</b></i>
        i. if x receives a proposal from y, then
            (a) he rejects it at once if he already holds a better proposal 
            (b) he holds it for consideration otherwise, simultaneously rejecting 
                any poorer proposal that he currently holds
        ii. An individual x proposes to the others in the order in which they 
            appear in his preference list, stopping when a promise of consideration 
            is received; any subsequent rejection causes x to continue immediately 
            his sequence of proposals.
        &nbsp;
        <code>
        <b>begin</b>
        proposer:= person
        repeat
            proposer proposes to his next_choice
            if next_choice has no request yet
                accept proposer's proposal
            else:
                if proposer is preferred:
                    proposer's next_choice rejects previous proposal
                rejected person proposes to next_choice
        <b>end</b>
        </code>
        &nbsp;
        Phase one terminates with either
        1. every person holding a proposal , or
        2. with one person rejected by everyone (No stable matching exists in this case)
        &nbsp;   
        <i><b>Phase two:</b></i>
        i. reduce the preference lists of each person by removing all the persons 
           poorer than their proposal simultaneously
        ii. Eliminate cycles from the preference lists
            1. set p(0) = person with more than one preferences in reduced list
            2. set q(0) = second preference of p(0)
            3. set p(i+1) = last preference of q(i)
            4. set q(i+1) = second preference of p(i+1)
            5. if a x is found such that x is in p(0...i):
                simultaneously reject q(i) and p(i+1) to eliminate cycle
            6. repeat until no cycles are found
      </pre>
    </p>
  </body>
</html>
