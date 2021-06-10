# Columns to use, as a list (to be edited & better formatted later)

FEATURES_TO_USE = {
  "FACILITY_RECODE" : [50],
  "MOTHERS_AGE_RECODE": [79],
  "MARITAL_STATUS": [120],
  "MOTHERS_EDUCATION": [124],
  "PRIOR_BIRTHS_NOW_LIVING": [171, 172],
  "PRIOR_BIRTHS_NOW_DEAD": [173, 174],
  "PRIOR_OTHER_TERMINATIONS": [175, 176],
  "LIVE_BIRTH_ORDER_RECODE": [179],
  "TOTAL_BIRTH_ORDER_RECODE": [182],
  "INTERVAL_SINCE_LAST_LIVE_BIRTH_RECODE": [198, 199, 200], # 888 = FIRST BIRTH, 999 = UNKNOWN OR NOT STATED
  "MONTH_PRENATAL_CARE_BEGAN_RECODE": [227],
  "NUMBER_OF_PRENATAL_VISITS_RECODE": [242, 243],
  "CIGARETTES_BEFORE_PREGNANCY_RECODE": [261],
  "CIGARETTES_FIRST_TRIMESTER_RECODE": [262],
  "CIGARETTES_SECOND_TRIMESTER_RECODE": [263],
  "CIGARETTES_THIRD_TRIMESTER_RECODE": [264],
  "MOTHERS_HEIGHT_IN_TOTAL_INCHES": [280, 281],
  "BMI_RECODE": [287],
  "PRE_PREGNANCY_WEIGHT_RECODE": [292, 293, 294],
  "DELIVERY_WEIGHT_RECODE": [299, 300, 301],
  "WEIGHT_GAIN": [304, 305],
  "PRE_PREGNANCY_DIABETES": [313],
  "GESTATIONAL_DIABETES": [314],
  "PRE_PREGNANCY_HYPERTENSION": [315],
  "GESTATIONAL_HYPERTENSION": [316],
  "HYPERTENSION_ECLAMPSIA": [317],
  "PREVIOUS_PRETERM_BIRTH": [318],
  "PREVIOUS_CESAREAN": [331],
  "NUMBER_OF_PREVIOUS_CESAREANS": [332, 333],
  "NO_INFECTIONS_REPORTED": [353],
  "INDUCTION_OF_LABOR": [383],
  "AUGMENTATION_OF_LABOR": [384],
  "CHORIOAMNIONITIS": [387],
  "ATTENDANT_AT_BIRTH": [433],
  "PAYMENT_SOURCE_FOR_DELIVERY": [435],
  "PLURALITY_RECODE": [454],
  "SEX_OF_INFANT": [475],
  "COMBINED_GESTATION_RECODE": [492, 493], # 99 if unknown
  "BIRTH_WEIGHT_RECODE": [509, 510],
  "TOL_ATTEMPTED": [403],
  "DELIVERY_METHOD_1": [407],
  "DELIVERY_METHOD_2": [408],
}


REPORTING_FLAGS = {
  "MOTHERS_EDUCATION": 126,
  "MONTH_PRENATAL_CARE_BEGAN_RECODE": 226,
  "NUMBER_OF_PRENATAL_VISITS_RECODE": 244,
  "CIGARETTES_BEFORE_PREGNANCY_RECODE": 265,
  "CIGARETTES_FIRST_TRIMESTER_RECODE": 266,
  "CIGARETTES_SECOND_TRIMESTER_RECODE": 267,
  "CIGARETTES_THIRD_TRIMESTER_RECODE": 268,
  "MOTHERS_HEIGHT_IN_TOTAL_INCHES": 282,
  "PRE_PREGNANCY_WEIGHT_RECODE": 295,
  "DELIVERY_WEIGHT_RECODE": 303,
  "WEIGHT_GAIN": 307,
  "PRE_PREGNANCY_DIABETES": 319,
  "GESTATIONAL_DIABETES": 320,
  "PRE_PREGNANCY_HYPERTENSION": 321,
  "GESTATIONAL_HYPERTENSION": 322,
  "HYPERTENSION_ECLAMPSIA": 323,
  "PREVIOUS_PRETERM_BIRTH": 324,
  "PREVIOUS_CESAREAN": 335,
  "NUMBER_OF_PREVIOUS_CESAREANS": 336,
  "INDUCTION_OF_LABOR": 389,
  "AUGMENTATION_OF_LABOR": 390,
  "CHORIOAMNIONITIS": 393,
  "PAYMENT_SOURCE_FOR_DELIVERY": 437,
  "COMBINED_GESTATION_RECODE": 498,
  "TOL_ATTEMPTED": 406,
  "DELIVERY_METHOD_1": 409,
  "DELIVERY_METHOD_2": 409,
}

