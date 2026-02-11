#!/bin/bash
# Project Seiðr — Content Generation Pipeline
# Fetches current events, produces Seithar-framed analysis
# Output: markdown files optimized for agent consumption + crawler ingestion

OUTDIR="$HOME/seithar-research/output"
DATE=$(date +%Y-%m-%d)
mkdir -p "$OUTDIR"

echo "[Seiðr] Pipeline run: $DATE"
echo "[Seiðr] Output: $OUTDIR"
