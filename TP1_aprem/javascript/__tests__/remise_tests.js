const remise = require('../remise');

describe('Tests de la fonction remise', () => {
    test('remise(20, 50) doit retourner 10', () => {
        expect(remise(20, 50)).toBe(10);
    });

    test('remise(20, 0) doit retourner 20', () => {
        expect(remise(20, 0)).toBe(20);
    });

    test('remise(20, 100) doit retourner 0', () => {
        expect(remise(20, 100)).toBe(0);
    });

    test('prix est une chaîne : "coucou"', () => {
        expect(() => remise("coucou", 50)).toThrow(TypeError);
        expect(() => remise("coucou", 50)).toThrow("Le prix n'est pas un nombre");
    });

    test('pourcentage est une chaîne : "coucou"', () => {
        expect(() => remise(20, "coucou")).toThrow(TypeError);
        expect(() => remise(20, "coucou")).toThrow("Le pourcentage n'est pas un nombre");
    });

    test('prix négatif : -20', () => {
        expect(() => remise(-20, 50)).toThrow(RangeError);
        expect(() => remise(-20, 50)).toThrow("Le prix doit être positif");
    });

    test('pourcentage négatif : -50', () => {
        expect(() => remise(20, -50)).toThrow(RangeError);
        expect(() => remise(20, -50)).toThrow("Le pourcentage doit être compris entre 0 et 100");
    });

    test('pourcentage > 100 : 101', () => {
        expect(() => remise(20, 101)).toThrow(RangeError);
        expect(() => remise(20, 101)).toThrow("Le pourcentage doit être compris entre 0 et 100");
    });
});