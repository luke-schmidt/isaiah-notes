#!/bin/bash
# build.sh
echo "Compiling Isaiah Guide..."

# Add MacTeX to PATH if it exists
if [ -d "/usr/local/texlive/2025" ]; then
    export PATH="/usr/local/texlive/2025/bin/universal-darwin:$PATH"
elif [ -d "/usr/local/texlive/2024" ]; then
    export PATH="/usr/local/texlive/2024/bin/universal-darwin:$PATH"
elif [ -d "/Library/TeX/texbin" ]; then
    export PATH="/Library/TeX/texbin:$PATH"
fi

xelatex -output-directory=output main.tex

if [ $? -eq 0 ]; then
    echo "✅ PDF generated successfully in output/main.pdf"
    
    # Generate preview image for visual testing
    if command -v convert >/dev/null 2>&1; then
        echo "📸 Generating preview image..."
        convert -density 150 output/main.pdf[0] output/preview.png
        if [ $? -eq 0 ]; then
            echo "✅ Preview generated: output/preview.png"
        else
            echo "⚠️  Preview generation failed (ImageMagick issue)"
        fi
    elif command -v pdftoppm >/dev/null 2>&1; then
        echo "📸 Generating preview image..."
        pdftoppm -png -singlefile -r 150 output/main.pdf output/preview
        if [ $? -eq 0 ]; then
            echo "✅ Preview generated: output/preview.png"
        else
            echo "⚠️  Preview generation failed (poppler issue)"
        fi
    else
        echo "ℹ️  Install ImageMagick or poppler-utils for automatic preview generation"
    fi
else
    echo "❌ Compilation failed."
    exit 1
fi