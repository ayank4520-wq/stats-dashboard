from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# ---- Statistics functions (same math as your earlier stats project) ----

def calculate_mean(nums):
    return sum(nums) / len(nums)


def calculate_median(nums):
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]


def calculate_mode(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    max_count = max(counts.values())
    modes = [n for n, c in counts.items() if c == max_count]
    return modes if max_count > 1 else None


def calculate_variance(nums):
    m = calculate_mean(nums)
    return sum((n - m) ** 2 for n in nums) / len(nums)


def calculate_std_dev(nums):
    return calculate_variance(nums) ** 0.5


def coefficient_of_variation(nums):
    return (calculate_std_dev(nums) / calculate_mean(nums)) * 100


# ---- Routes ----

@app.route('/')
def home():
    # Renders templates/index.html
    return render_template('index.html')


@app.route('/api/stats', methods=['POST'])
def get_stats():
    data = request.get_json()
    nums = data.get('numbers', [])

    # Basic validation — always check what the frontend sends you
    if not isinstance(nums, list) or len(nums) < 2:
        return jsonify({'error': 'Please provide at least 2 numbers'}), 400

    try:
        nums = [float(n) for n in nums]
    except (ValueError, TypeError):
        return jsonify({'error': 'All values must be numbers'}), 400

    result = {
        'numbers': nums,
        'count': len(nums),
        'mean': round(calculate_mean(nums), 2),
        'median': calculate_median(nums),
        'mode': calculate_mode(nums),
        'min': min(nums),
        'max': max(nums),
        'range': round(max(nums) - min(nums), 2),
        'variance': round(calculate_variance(nums), 2),
        'std_dev': round(calculate_std_dev(nums), 2),
        'cv': round(coefficient_of_variation(nums), 1)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
