from Editex_code import Editex 

#Name which is compared among the available ones
main_name = "Ztivenson"
#Random generated names for testing
available_names = ["Jonson", "Adams", "Davies", "Simmons", "Richardson", "Tailor", "Chater", "Stephenson", "Naylor", "Smythe", "MacDonald", "Harrys", "Sym", "Wilson", "Barker", "Wills", "Frazer", "Johns", "Wilkinson", "Hunter", "Saunders", "Pearson", "Robertson", "Parker"]

result = [[0, 1] for _ in range(len(available_names))]

editex = Editex()
for num in range(len(available_names)):
    sim_value = editex.get_sim_score(main_name, available_names[num])
    result[num][0] = available_names[num]
    result[num][1] = sim_value

result = sorted(result, key=lambda x: x[1], reverse=True)

for x in result:
    print(x)
    

