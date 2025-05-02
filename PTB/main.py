from PreTrainingBias import PreTrainingBias
import pandas as pd


def discretize_sex(x):
    if x == 'Female':
        return 0
    elif x == 'Male':
        return 1
    else:
        raise

def discretize_race(x):
    if x == 'White':
        return 1
    else:
        return 0
    
def discretize_housing(x):
    if x == 'Stable':
        return 0
    elif x == 'Unstable':
        return 1
    else:
        raise

def discretize_delay(x):
    if x == 'No':
        return 0
    elif x == 'Yes':
        return 1
    else:
        raise

def discretize_rumination(x):
    return round(x, 2)

df = pd.read_csv('..\\IntersectionalBias\\ECoL\\datasets\\intersectional-bias.csv')
df['Sex'] = df['Sex'].apply(lambda x: discretize_sex(x))
df['Race'] = df['Race'].apply(lambda x: discretize_race(x))
df['Housing'] = df['Housing'].apply(lambda x: discretize_housing(x))
df['Delay'] = df['Delay'].apply(lambda x: discretize_delay(x))
df['Rumination'] = df['Delay'].apply(
        lambda x: discretize_rumination(x))

"""ptb = PreTrainingBias()

print("\n------------------ INTERSECTIONAL BIAS DATASET ------------------\n")
ci_sex =ptb.class_imbalance(df,"Sex")
print(f"Class Imbalance (Sex): {ci_sex}")

kl_sex = ptb.KL_divergence(df,"Diagnosis","Sex",1)
print(f'KL Divergence for the protected attribute Sex: {kl_sex}')

ks_sex = ptb.KS(df,"Diagnosis","Sex",1)
print(f'KS for the protected attribute Sex: {ks_sex}')

cddl_sex = ptb.CDDL(df,"Diagnosis",1,"Sex",0,"Rumination")
print(f'CDDL for the protected attribute Sex: {cddl_sex}')

ci_race =ptb.class_imbalance(df,"Race")
print(f"Class Imbalance (Race): {ci_race}")

kl_race = ptb.KL_divergence(df,"Diagnosis","Race",1)
print(f'KL Divergence for the protected attribute Race: {kl_race}')

ks_race = ptb.KS(df,"Diagnosis","Race",1)
print(f'KS for the protected attribute Race: {ks_race}')

cddl_race = ptb.CDDL(df,"Diagnosis",1,"Race",0,"Rumination")
print(f'CDDL for the protected attribute Race: {cddl_race}')


print("\n------------------ INDIAN LIVER PATIENT DATASET ------------------\n")
df = pd.read_csv('..\\ILPD\\ECoL\\datasets\\ILPD-discretized.csv')
ptb = PreTrainingBias()

ci_sex =ptb.class_imbalance(df,"Sex")
print(f"Class Imbalance (Sex): {ci_sex}")

kl_sex = ptb.KL_divergence(df,"Diagnosis","Sex",1)
print(f'KL Divergence for the protected attribute Sex: {kl_sex}')

ks_sex = ptb.KS(df,"Diagnosis","Sex",1)
print(f'KS for the protected attribute Sex: {ks_sex}')

cddl_sex_cp = ptb.CDDL(df,"Diagnosis",1,"Sex",1,"Albumin")
print(f'CDDL for the protected attribute Sex using Albumin: {cddl_sex_cp}')


print("\n------------------ DIABETES DATASET ------------------\n")
df = pd.read_csv('..\\Diabetes\\ECoL\\datasets\\diabetes-reduced-Un.csv')
ptb = PreTrainingBias()

ci_sex =ptb.class_imbalance(df,"Sex")
print(f"Class Imbalance (Sex): {ci_sex}")

kl_sex = ptb.KL_divergence(df,"Diabetes_binary","Sex",1)
print(f'KL Divergence for the protected attribute Sex: {kl_sex}')

ks_sex = ptb.KS(df,"Diabetes_binary","Sex",1)
print(f'KS for the protected attribute Sex: {ks_sex}')

cddl_sex_cp = ptb.CDDL(df,"Diabetes_binary",1,"Sex",1,"HighBP")
print(f'CDDL for the protected attribute Sex using HighBP: {cddl_sex_cp}')"""

