m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

all_count, all_sum, all_averege, tuple_all  = sum([len(i) for i in m]),sum([sum(i) for i in m]),sum([sum(i) for i in m])/sum([len(i) for i in m]),tuple( j for i in m for j in i)

print('1.',all_count)
print('2.',all_sum)
print('3.', all_averege)
print('4.',tuple_all)