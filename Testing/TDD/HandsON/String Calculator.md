

https://osherove.com/tdd-kata-1

```ts

// File: StringCalculator.ts
export class StringCalculator {
    private callCount = 0;
    public static readonly DEFAULT_DELIMITERS = [',', '\n'];

    public Add(input: string): number {
        this.callCount++;

        if (!input) return 0;

        let delimiters = [...StringCalculator.DEFAULT_DELIMITERS];
        if (input.startsWith("//")) {
            const match = input.match(/^\/\/(\[.*?\]|.)\n/);
            if (match) {
                const customDelimiter = match[1];
                input = input.slice(match[0].length);
                delimiters = this.parseDelimiters(customDelimiter);
            }
        }

        const numbers = this.parseNumbers(input, delimiters);

        this.validateNumbers(numbers);

        return numbers
            .filter((num) => num <= 1000) // Ignore numbers > 1000
            .reduce((sum, num) => sum + num, 0);
    }

    public GetCalledCount(): number {
        return this.callCount;
    }

    private parseDelimiters(customDelimiter: string): string[] {
        if (customDelimiter.startsWith("[")) {
            return customDelimiter
                .slice(1, -1)
                .split("][");
        }
        return [customDelimiter];
    }

    private parseNumbers(input: string, delimiters: string[]): number[] {
        const regex = new RegExp(`[${delimiters.map((d) => d.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')).join('|')}]`);
        return input
            .split(regex)
            .map((value) => parseInt(value, 10))
            .filter((num) => !isNaN(num));
    }

    private validateNumbers(numbers: number[]): void {
        const negatives = numbers.filter((num) => num < 0);
        if (negatives.length) {
            throw new Error(`negatives not allowed: ${negatives.join(", ")}`);
        }
    }
}

// File: StringCalculator.test.ts
import { StringCalculator } from "./StringCalculator";

describe("StringCalculator", () => {
    let calculator: StringCalculator;

    beforeEach(() => {
        calculator = new StringCalculator();
    });

    it("should return 0 for an empty string", () => {
        expect(calculator.Add("")).toBe(0);
    });

    it("should return the number itself for a single number input", () => {
        expect(calculator.Add("1")).toBe(1);
    });

    it("should return the sum for two numbers separated by a comma", () => {
        expect(calculator.Add("1,2")).toBe(3);
    });

    it("should handle an unknown number of numbers", () => {
        expect(calculator.Add("1,2,3,4,5")).toBe(15);
    });

    it("should handle new lines between numbers", () => {
        expect(calculator.Add("1\n2,3")).toBe(6);
    });

    it("should support different delimiters", () => {
        expect(calculator.Add("//;\n1;2")).toBe(3);
    });

    it("should throw an exception for negative numbers", () => {
        expect(() => calculator.Add("1,-2,3,-4")).toThrow("negatives not allowed: -2, -4");
    });

    it("should ignore numbers greater than 1000", () => {
        expect(calculator.Add("2,1001,6")).toBe(8);
    });

    it("should handle delimiters of any length", () => {
        expect(calculator.Add("//[***]\n1***2***3")).toBe(6);
    });

    it("should handle multiple delimiters", () => {
        expect(calculator.Add("//[*][%]\n1*2%3")).toBe(6);
    });

    it("should handle multiple delimiters with length longer than one character", () => {
        expect(calculator.Add("//[**][%%]\n1**2%%3")).toBe(6);
    });

    it("should count the number of times Add is called", () => {
        calculator.Add("1,2");
        calculator.Add("3,4");
        expect(calculator.GetCalledCount()).toBe(2);
    });
});


```