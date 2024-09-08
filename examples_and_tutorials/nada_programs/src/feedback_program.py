from nada_dsl import *
import nada_numpy as na

def nada_main():

    # 1. Parties initialization
    suborganiser1 = Party(name="SubOrganiser1")
    suborganiser2 = Party(name="SubOrganiser2")
    suborganiser3 = Party(name="SubOrganiser3")
    outparty = Party(name="participant1")

    # 2. Inputs initialization
    ## Votes from voter 0
    feedback1 = SecretInteger(Input(name="feedback1", party=suborganiser1))
    feedback2 = SecretInteger(Input(name="feedback2", party=suborganiser2))
    feedback3 = SecretInteger(Input(name="feedback3", party=suborganiser3))

    # 3. Computation
    ## Add votes for candidate 0
    avg_feedback = feedback1 + feedback2 + feedback3

    # 4. Output
    output_score = Output(avg_feedback, "avg_feedback", party=outparty)

    return [output_score]
