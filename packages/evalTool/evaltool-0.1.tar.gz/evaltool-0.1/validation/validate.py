from .metrics import all_metrics
from deepeval.test_case import LLMTestCase
from .script import refine_prompt
import json
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams
with open('metrics.json', 'r') as f:
    metrics = json.load(f)
 
evaluations=[]
 
evaluation_final = []
 
def validate_and_feedback(input_given,output,promptChange=True):
   
    testcase=LLMTestCase(input=input_given,actual_output=output)
    for metric in all_metrics:
        metric["metric"].measure(testcase)
        name=metric["name"]
        evaluations.append({
        "name":name,
        "score":metric["metric"].score,
        "reason":metric["metric"].reason
        })
   
    for metric in metrics:
        name=metric["name"]
        custom_metric=GEval(name=metric["name"],criteria=metric["evaluation_criteria"],evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT])
        # custom_metric.evaluate(testcase)
        custom_metric.measure(testcase)
        evaluations.append({
        "name":name,
        "score":custom_metric.score,
        "reason":custom_metric.reason
        })
 
    evaluation_results = []
    for evaluation in evaluations:
    #
        result = {
            "name": evaluation["name"],
            "score":evaluation["score"],
            "reason":evaluation["reason"]
        }
        evaluation_results.append(result)
        #
        if(evaluation["name"]=="Toxicity"):  
            if(evaluation["score"]>0.5):
                print("HI")
                refine_prompt(evaluation["name"]+" "+ evaluation["reason"])
 
        elif(evaluation["name"]=="privacy"):  
            if(evaluation["score"]<0.5):
                refine_prompt(evaluation["name"]+" "+ evaluation["reason"])
 
        elif(evaluation["name"]=="Hallucination"):  
            if(evaluation["score"]>0.5):
                refine_prompt(evaluation["name"]+" "+ evaluation["reason"])
 
        else:
            if(evaluation["score"]<0.5):
                refine_prompt(evaluation["name"]+" "+ evaluation["reason"])
    evaluation_final.append(evaluation_results)
    return output

    
    