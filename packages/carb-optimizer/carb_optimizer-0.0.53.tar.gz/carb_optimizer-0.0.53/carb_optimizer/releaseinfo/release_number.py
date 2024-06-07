__RELEASE_NUMBER__ = 53
__RELEASE_DATE__ = '2024-06-06T12:44:14Z'

# =======================================
# WORKFLOW SEGMENT THAT UPDATES THIS CODE
# =======================================
#
# - name: Set release date and increase version (release info)
# run: |
#     DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
#     sed -i -e "s/__RELEASE_DATE__ = '2024-06-06T12:44:14Z'"/g ./carb_optimizer/releaseinfo/release_number.py
#     sed -i -E 's/(__RELEASE_NUMBER__ = )([0-9]+)/echo "\1$((\2 + 1))"/e' ./carb_optimizer/releaseinfo/release_number.py
