str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
   if s:
        res_list.append(s)
print(res_list)