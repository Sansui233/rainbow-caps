# -*- coding: utf-8 -*-
import csv
import json


def genRecipeItem(item: dict, extranbt_kv: str):
    # 有 buy buyB(optinal) sell 三个字段

    recipesobj = "{rewardExp:0b, maxUses:1000,"

    recipesobj += 'buy:{{id:"{}",Count:{}}}'.format(
        item["buy"]["id"], item["buy"]["Count"]
    )
    if "buyB" in item:
        recipesobj += ',buyB:{{id:"{}",Count:{}}}'.format(
            item["buyB"]["id"], item["buyB"]["Count"]
        )
    extranbt_kv = (
        ",{}".format(extranbt_kv) if "AttributeModifiers" in item["sell"]["tag"] else ""
    )
    recipesobj += (
        ",sell:"
        + "{"
        + 'id:"{}"'.format(item["sell"]["id"])
        + ",Count:{}".format(item["sell"]["Count"])
        + ",tag:"
        + "{"
        + "CustomModelData:{}".format(item["sell"]["tag"]["CustomModelData"])
        + ",display:"
        + "{"
        + "Name:'{}'".format(
            json.dumps(item["sell"]["tag"]["display"]["Name"], ensure_ascii=False)
        )
        + "}"
        + extranbt_kv
        + "}"
        + "}"
    )

    recipesobj = recipesobj + "}"
    return recipesobj


with open("scripts/trades.csv", "r+", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)  # skip the headers
    new_objects: list[dict] = []
    for row in reader:
        newobject: dict = {
            "buy": {"id": row[0], "Count": row[1] + "b"},
            "buyB": {"id": row[2], "Count": row[3] + "b"},
            "sell": {
                "id": row[4],
                "Count": "1b",
                "tag": {
                    "CustomModelData": row[6],
                    "display": {"Name": {"text": row[5], "italic": False}},
                },
            },
        }
        if row[7] == "true":
            newobject["sell"]["tag"]["AttributeModifiers"] = []
        new_objects.append(newobject)

    recipeobj = {"Recipes": new_objects}

    with open("scripts/list.json", "w", encoding="utf-8") as output:
        json.dump(recipeobj, output, ensure_ascii=False)


with open("scripts/list.json", "r+", encoding="utf-8") as f:
    with open("scripts/extranbt.txt", "r+", encoding="utf-8") as nbtfile:
        # 处理盔甲值的字符串
        extranbt_kv = nbtfile.readlines()
        for i, line in enumerate(extranbt_kv):
            extranbt_kv[i] = line.strip()
        extranbt_kv = "".join(extranbt_kv)  # 结尾没有逗号

        # 处理交易数据
        data = json.load(f)
        itemLists = [genRecipeItem(item, extranbt_kv) for item in data["Recipes"]]
        recipesobj = "{" + "Recipes:[{}]".format(",".join(itemLists)) + "}"

        nbtobj = (
            "{NoGravity:1b,"
            + "Silent:1b,Invulnerable:1b,"
            + "PersistenceRequired:1b,"
            + "NoAI:1b,"
            + "Willing:1b,"
            + 'Tags:["block_trader","carved_pumpkin"],'
            + 'ArmorItems:[{},{},{},{id:"minecraft:carved_pumpkin",Count:1b,tag:{CustomModelData:100}}],'
            + "Offers:{}".format(recipesobj)
            + "}"
        )
        command = "summon minecraft:wandering_trader ~0.5 ~-1 ~0.5 {}".format(nbtobj)

        with open("scripts/conmmand.txt", "w", encoding="utf-8") as output:
            output.write(command)
