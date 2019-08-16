from random import randint

local="breast-cancer/"

full_dataset = open(local+"breast-cancer-wisconsin.data.without_ids_nor_interrogations", "r")


train_set = open(local + "breast-cancer-wisconsin.data.train", "w")
test_set = open(local + "breast-cancer-wisconsin.data.test", "w")

test_set_size = 0

for line in full_dataset:

    r = randint(1,3)

    if 1 == r and test_set_size < 155:
        test_set.write(line)
        test_set_size += 1
    else:
        train_set.write(line)


train_set.close()
test_set.close()
full_dataset.close()
