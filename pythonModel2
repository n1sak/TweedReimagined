brand_cooccurrence = {}
for line in lines:
    line_clean = line.strip().lower()
    if line_clean and line_clean not in ['dnf', 'n/a', '']:
        brands_in_line = []
        for brand in brand_names:
            if brand.lower() in line_clean:
                brands_in_line.append(brand)
        
        # Record co-occurrences
        for i, brand1 in enumerate(brands_in_line):
            for brand2 in brands_in_line[i+1:]:
                pair = tuple(sorted([brand1, brand2]))
                if pair not in brand_cooccurrence:
                    brand_cooccurrence[pair] = 0
                brand_cooccurrence[pair] += 1

print("Brand Co-occurrence Analysis:")
if brand_cooccurrence:
    sorted_cooccurrence = sorted(brand_cooccurrence.items(), key=lambda x: x[1], reverse=True)
    print("Top brand pairs appearing together:")
    for pair, count in sorted_cooccurrence[:10]:
        print(pair[0] + " + " + pair[1] + ": " + str(count) + " times")
else:
    print("No significant brand co-occurrences found")

# 2. Analyze brand diversity by position
print("\
Brand Diversity Analysis:")
segment_diversity = []
for i in range(10):
    start_idx = i * segment_size
    end_idx = (i + 1) * segment_size if i < 9 else len(lines)
    segment = lines[start_idx:end_idx]
    
    unique_brands_in_segment = set()
    for line in segment:
        line_clean = line.strip().lower()
        for brand in brand_names:
            if brand.lower() in line_clean:
                unique_brands_in_segment.add(brand)
    
    segment_diversity.append(len(unique_brands_in_segment))

print("Brand diversity by segment:")
for i, diversity in enumerate(segment_diversity):
    print("Segment " + str(i+1) + ": " + str(diversity) + " unique brands")

avg_diversity = sum(segment_diversity) / len(segment_diversity)
print("Average brand diversity per segment: " + str(round(avg_diversity, 1)))
