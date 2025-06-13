function remise(prix, pourcentage) {
    if (typeof prix !== 'number') {
        throw new TypeError("Le prix n'est pas un nombre");
    }
    if (typeof pourcentage !== 'number') {
        throw new TypeError("Le pourcentage n'est pas un nombre");
    }
    if (prix < 0) {
        throw new RangeError("Le prix doit être positif");
    }
    if (pourcentage < 0 || pourcentage > 100) {
        throw new RangeError("Le pourcentage doit être compris entre 0 et 100");
    }
    return prix - ((prix * pourcentage) / 100);
}

module.exports = remise;