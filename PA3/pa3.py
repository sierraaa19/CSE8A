def get_shippable_pumpkins(pumpkin_weights, min_weight, max_weight):
    goodpumpkins = []
    for pumpkin in range(len(pumpkin_weights)):
        if pumpkin_weights[pumpkin] >=  min_weight and pumpkin_weights[pumpkin] <= max_weight:
            goodpumpkins = goodpumpkins + [pumpkin_weights[pumpkin]]
    return goodpumpkins



        
