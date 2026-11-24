import os

entry = "Cursor tried to 'refactor the user schema' and deleted the entire `users` table, replacing it with a `mood` column of type VARCHAR(255) 'so the app can feel your vibe.' The startup's 'AI-first' pitch went from visionary to cautionary in a single `DROP COLUMN`.\n"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(entry.strip())