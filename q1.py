# Problem: Create DataFrame from List
# Platform: LeetCode


import pandas as pd
from typing import List

def create_dataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df