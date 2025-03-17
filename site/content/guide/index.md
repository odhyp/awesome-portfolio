+++
title = "Guide"
description = "Want to showcase your portfolio? Follow this guide to add your project and help grow the collection!"
layout = "single"
+++

## Step 1: Fork the Repository

1. Visit the [Awesome Portfolio] repository on GitHub and click the **Fork** button at the top right corner. This will create a copy of the repository under your GitHub account.

2. Clone the forked repository to your local machine. Open your terminal and run:

    ```bash
    git clone https://github.com/your-username/awesome-portfolio.git
    ```

3. Navigate into the project directory

    ```bash
    cd awesome-portfolio
    ```

## Step 2: Add Your Portfolio to the Table

1. Open the README.md file in your preferred code editor
2. Locate the Portfolio Table section
3. Add a new row at the end of the table with your portfolio details

## Step 3: Fill in Portfolio Details

The portfolio list uses a markdown table format. Your new row should follow this structure:

```md
| Author Name | Live URL | Source URL | Tech Stacks |
```

Fill in the required details as follows:

### Column 1: Author Name

Your name or the creator's name. Example:

```md
Odhy Pradhana
```

### Column 2: Live URL

The direct link to the portfolio website. Example:

```md
[odhyp.com](https://odhyp.com/)
```

### Column 3: Source URL

If available, add the GitHub repository link. If closed-source, use an author profile link or write `None`.

```md
# Using repository link
[GitHub](https://github.com/odhyp/odhyp.com)

# Using author profile link
[GitHub](https://github.com/odhyp)

# If unavailable (not recommended)
None
```

### Column 4: Tech Stack

List the technologies used, separated by commas. Example:

```md
TypeScript, Next.js, TailwindCSS, Vercel
```

### Recap: Your Row Should Look Like This

```md
| Odhy Pradhana | [odhyp.com](https://odhyp.com/) | [GitHub](https://github.com/odhyp/odhyp.com) | TypeScript, Next.js, TailwindCSS, Vercel |
```

> **Note**: You don't need to adjust the column width. Just maintain the `|` separators.

## Step 4: Commit & Create a Pull Request

1. Stage and commit your changes:

    ```bash
    git add README.md
    git commit -m "portfolio: add <author name>"
    ```

2. Push the changes to your forked repository:

    ```bash
    git push origin master
    ```

3. Create a Pull Request
    - Go to the original [Awesome Portfolio] repository
    - Click New Pull Request
    - Fill in the Pull Request template
    - Click submit

## Final Step 🎉

Congratulations! Your submission will be reviewed and merged soon. Stay tuned for updates! 🚀

## Need Help?

If you have any questions, feel free to ask in the Discussions below or create a new [Issues].

[Awesome Portfolio]: https://github.com/odhyp/awesome-portfolios/
[Issues]: https://github.com/odhyp/awesome-portfolio/issues
