# -*- coding: utf-8 -*-

# Replace the merchant summon command according to trades.csv


import csv
import json


def genRecipeItem(item: dict, extranbt_kv: str) -> str:
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


def csv2listJson(
    csv_path="scripts/trades.csv", output_json_path="scripts/output/list.json"
):
    with open(csv_path, "r+", encoding="utf-8") as csvfile:
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

        with open(output_json_path, "w", encoding="utf-8") as output:
            json.dump(recipeobj, output, ensure_ascii=False)


def listJson2command(json_path="scripts/output/list.json") -> str:
    with open(json_path, "r+", encoding="utf-8") as f:
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
            command = "summon minecraft:wandering_trader ~0.5 ~-1 ~0.5 {} \n".format(
                nbtobj
            )

            with open("scripts/output/command.txt", "w", encoding="utf-8") as output:
                output.write(command)

            return command


def replaceCommand(
    command: str,
    mcfunction_file="data/merchants/functions/summon/carved_pumpkin.mcfunction",
):
    """
    replace the line after marker
    """
    marker = "# script marker"
    with open(mcfunction_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    marker_index = None
    for i, line in enumerate(lines):
        if line.startswith(marker):
            marker_index = i
            break

    if marker_index is not None:
        # replace
        if marker_index + 1 < len(lines):
            lines[marker_index + 1] = command
        # save
        with open(mcfunction_file, "w", encoding="utf-8") as file:
            file.writelines(lines)
        print("[Info] replace {} with new command".format(mcfunction_file))
    else:
        print("[Error] no marker found in {}".format(mcfunction_file))


if __name__ == "__main__":
    csv2listJson()
    command = listJson2command()
    replaceCommand(command)
