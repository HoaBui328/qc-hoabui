# Global Impact Matrix
- **Ngày check:** 2026-05-22
- **Phạm vi:** Report — 55 UC directories
- **CMR tham chiếu:** CMR_common_business_rules.md + Align_CMR_Report_20260520.md

| Tên File | Vị trí (Tên trường/Module) | Lỗi / Bất đồng bộ phát hiện | Current Text (Nội dung cũ) | Target Text (Đề xuất nội dung chuẩn) | Trạng thái |
|---|---|---|---|---|---|
| `UC299-304_bieu-tong-hop-kkt_audited_20260508_v4.md` L99 | Validate khi Nộp — Error message | [CMR_CONFLICT] Dùng "Trường bắt buộc" thay vì chuẩn CMR_06 STD-02 | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC299-304_bieu-tong-hop-kkt_audited_20260508_v4.md` L105 | Validation Table — Text fields | [CMR_CONFLICT] Error message sai chuẩn + max length cũ | `Max 500 ký tự / "Trường bắt buộc"` | `Max 255 ký tự / "Vui lòng nhập [tên trường]"` | `Pending` |
| `UC299-304_bieu-tong-hop-kkt_audited_20260508_v4.md` L106 | Validation Table — KKT dropdown | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng chọn [tên trường]"` | `Pending` |
| `UC299-304_bieu-tong-hop-kkt_audited_20260508_v4.md` L131 | AC-02 — Validate bắt buộc nộp | [CMR_CONFLICT] AC dùng text cũ | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC335-340_ChiSoDanhGiaHieuQuaKCNST_audited_20260514_v1.md` L257 | BR11 — Nộp báo cáo | [CMR_CONFLICT] Error message V01 sai chuẩn | `Lỗi inline V01: "Trường bắt buộc"` | `Lỗi inline V01: "Vui lòng nhập [tên trường]"` | `Pending` |
| `UC335-340_ChiSoDanhGiaHieuQuaKCNST_audited_20260514_v1.md` L269 | Validation Codes Table — V01 | [CMR_CONFLICT] Định nghĩa V01 sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC335-340_ChiSoDanhGiaHieuQuaKCNST_audited_20260514_v1.md` L338 | AC-12 — Bỏ trống trường bắt buộc | [INTRA_DOC_CONFLICT] AC không khớp Target V01 | `Lỗi inline V01 "Trường bắt buộc"` | `Lỗi inline V01 "Vui lòng nhập [tên trường]"` | `Pending` |
| `UC335-340_ChiSoDanhGiaHieuQuaKCNST_audited_20260514_v2.md` L257 | BR11 — Nộp báo cáo | [CMR_CONFLICT] Bản v2 vẫn còn lỗi | `Lỗi inline V01: "Trường bắt buộc"` | `Lỗi inline V01: "Vui lòng nhập [tên trường]"` | `Pending` |
| `UC215-220_ChuyenVonDTRNN_audited_v1.md` L163 | Validation Table — Số văn bản | [CMR_CONFLICT] Error message sai + max length lệch v2 | `Max 50 ký tự / "Trường bắt buộc"` | `Max 255 ký tự / "Vui lòng nhập Số văn bản"` | `Pending` |
| `UC215-220_ChuyenVonDTRNN_audited_v1.md` L164 | Validation Table — Năm báo cáo | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập Năm báo cáo"` | `Pending` |
| `UC215-220_ChuyenVonDTRNN_audited_v1.md` L165 | Validation Table — Tên NĐT, Mã DN... | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC203-208_QLNNBoDTRNN_audited_20260511_v1.md` L113 | AC_FN_03 — Nộp thiếu trường | [CMR_CONFLICT] AC text sai chuẩn | `inline đỏ "Trường bắt buộc"` | `inline đỏ "Vui lòng nhập [tên trường]"` | `Pending` |
| `UC203-208_QLNNBoDTRNN_audited_20260511_v2.md` L113 | AC_FN_03 — Nộp thiếu trường | [CMR_CONFLICT] Bản v2 vẫn còn lỗi | `inline đỏ "Trường bắt buộc"` | `inline đỏ "Vui lòng nhập [tên trường]"` | `Pending` |
| `UC209-214_DKGDNHChamDutDTRNN_audited_20260511_v1.md` L143 | AC — Validate Số văn bản | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập Số văn bản"` | `Pending` |
| `UC209-214_DKGDNHChamDutDTRNN_audited_20260511_v2.md` L143 | AC — Validate Số văn bản | [CMR_CONFLICT] Bản v2 vẫn còn lỗi | `"Trường bắt buộc"` | `"Vui lòng nhập Số văn bản"` | `Pending` |
| `UC191-196_BaoCaoNamTaiChinhDTRNN_audited_20260511_v1.md` L144 | AC — Validate Nộp | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC191-196_BaoCaoNamTaiChinhDTRNN_audited_20260511_v1.md` L151 | Validation Table — Trường bắt buộc | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC191-196_BaoCaoNamTaiChinhDTRNN_audited_20260511_v1.md` L185 | AC-04 — Validate trường bắt buộc | [INTRA_DOC_CONFLICT] AC không khớp chuẩn V01 | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC185-190_BaoCaoNamDTRNN_audited_20260511_v1.md` L125 | Validation Table — Text/Textarea | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc" (V01)` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC185-190_BaoCaoNamDTRNN_audited_20260511_v1.md` L156 | AC-04 — Lý do / giải pháp | [INTRA_DOC_CONFLICT] AC dùng text cũ | `Lỗi inline "Trường bắt buộc" (V01)` | `Lỗi inline "Vui lòng nhập Lý do / giải pháp"` | `Pending` |
| `UC113-118_XuatKhauDTNN_audited_v5.md` L210 | AC-09 — Validate bắt buộc | [CMR_CONFLICT] Error message sai chuẩn | `"Trường bắt buộc"` | `"Vui lòng nhập [tên trường]"` | `Pending` |
| `UC329-334_ThuHoiDuAnKCN.md` L51 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai vs CS_01 | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC329-334_ThuHoiDuAnKCN.md` L75 | Search section — Empty State detail | [CMR_CONFLICT] Dùng "màn hình trắng" sai CS_01 | `màn hình trắng + "Không tìm thấy kết quả"` | `Icon + "Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC329-334_bieu-thu-hoi-du-an-kcn_audited_20260521_v2.md` L112 | UI Inventory — Empty state msg | [CMR_CONFLICT] Chưa cập nhật sau Align | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC329-334_bieu-thu-hoi-du-an-kcn_audited_20260521_v2.md` L162 | Search bar filter #3 | [CMR_CONFLICT] Empty State sai chuẩn | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC323-328_DieuChinhDuAnKCN.md` L53 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC305-310_BieuKhuPhiThueQuan.md` L57 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC299-304_BieuTongHopKKT.md` L69 | Search bar — Empty State | [CMR_CONFLICT] Empty State text + màn hình trắng | `màn hình trắng + "Không tìm thấy kết quả"` | `Icon + "Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC347-352_ChiSoDanhGiaDNSinhThai.md` L60 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC341-346_GiamSatKCNSinhThai.md` L60 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC335-340_ChiSoDanhGiaHieuQuaKCNST.md` L60 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC233-238_BaoCaoTruocKhiThucHienDuAnDT_v1.1.md` L54 | Search bar — Empty State | [CMR_CONFLICT] Empty State text + màn hình trắng | `màn hình trắng + "Không tìm thấy kết quả"` | `Icon + "Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC221-226_audited-v1.md` L204 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC221-226_audited-v2.md` L205 | Search bar — Empty State | [CMR_CONFLICT] Bản v2 vẫn còn lỗi | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC209-214_DKGDNHChamDutDTRNN.md` L49 | Search bar — Empty State | [CMR_CONFLICT] Empty State text sai | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC191-196_BaoCaoNamTaiChinhDTRNN.md` L55 | Search bar — Empty State | [CMR_CONFLICT] Empty State + màn hình trắng sai | `màn hình trắng + "Không tìm thấy kết quả"` | `Icon + "Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC364-366_QuanLyBaoCaoDaNop.md` L133 | Empty State B — Search/filter | [CMR_CONFLICT] Text sai chuẩn CS_01 | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC367-372_QuanLyBaoCaoDaNhan.md` L150 | Empty State B — Search/filter | [CMR_CONFLICT] Text sai + thiếu icon | `"Không tìm thấy dữ liệu"` | `Icon + "Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC179-184_ChamDutHoatDongDTRNN_aligned_20260522_v1.md` L107 | Empty State — Danh sách | [CMR_CONFLICT] Text sai CS_01 | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC215-220_ChuyenVonDTRNN.md` L77 | Empty State — Filter/Search | [CROSS_UC_PARITY_CONFLICT] Text khác các UC cùng loại | `"Không tìm thấy kết quả phù hợp"` | `"Không tìm thấy dữ liệu phù hợp"` | `Pending` |
| `UC364-366_QuanLyBaoCaoDaNop.md` L85 | Search bar — Placeholder | [CROSS_UC_PARITY_CONFLICT] Từ ngữ lệch vs UC367-372 | `"Tìm kiếm nhanh theo mã hoặc tên báo cáo"` | `"Tìm kiếm nhanh theo mã báo cáo, tên báo cáo"` | `Pending` |
| `UC233-238_BaoCaoTruocKhiThucHienDuAnDT_v1.1.md` L54 | Search bar — Placeholder | [CROSS_UC_PARITY_CONFLICT] Từ ngữ lệch chuẩn | `"Tìm kiếm theo mã báo cáo, tên dự án"` | `"Tìm kiếm nhanh theo mã báo cáo, tên dự án"` (thêm "nhanh") | `Pending` |
| `UC367-372_QuanLyBaoCaoDaNhan.md` L263 | Popup Yêu cầu CS — Trường Lý do | [CROSS_UC_PARITY_CONFLICT] Max length lệch file _aligned (400 vs 3000) | `Max 400 ký tự` | `Max 3000 ký tự` (theo file aligned v1) | `Pending` |
| `UC329-334_bieu-thu-hoi-du-an-kcn_audited_20260521_v2.md` L248 | Validate — Trường số Cột 7,8 | [CMR_CONFLICT] Precision sai chuẩn CMR_05 C05b | `"tối đa 1 dấu chấm thập phân. Max 18 ký tự"` | `"Phần nguyên ≤15 chữ số, phần thập phân ≤5 chữ số"` | `Pending` |
| `UC329-334_bieu-thu-hoi-du-an-kcn_audited_20260521_v2.md` L248 | Error message V04 — Số sai định dạng | [CMR_CONFLICT] Dấu chấm cuối message vi phạm H-rule | `"Sai định dạng số."` | `"Sai định dạng số"` (bỏ dấu `.`) | `Pending` |
| `UC185-190_BaoCaoNamDTRNN_audited_20260511_v1.md` L126 | Validation — Trường số nhóm 1,3,4,5,6 | [CMR_CONFLICT] Dấu chấm cuối V04 message | `"Sai định dạng số." (V04)` | `"Sai định dạng số"` | `Pending` |
| `UC191-196_BaoCaoNamTaiChinhDTRNN_audited_20260511_v1.md` L152 | Validation — Trường số | [CMR_CONFLICT] Dấu chấm cuối V04 message | `"Sai định dạng số."` | `"Sai định dạng số"` | `Pending` |
| `UC155-160_GiaoDatChoThuedat.md` L130 | Diện tích (ha) Cột 3 | [CROSS_UC_PARITY_CONFLICT] Precision 2dp vs chuẩn 5dp của nhóm UC tài chính | `tối đa 2 chữ số thập phân` | `Tối đa 5 chữ số thập phân` (đồng bộ CMR_05) hoặc BA confirm | `Pending` |
| `UC215-220_ChuyenVonDTRNN.md` L116 | Vốn chuyển ra NN (USD) | [CROSS_UC_PARITY_CONFLICT] Precision 2dp, max value hardcode | `tối đa 2 chữ số thập phân; max value: 999,999,999,999.99` | `Phần nguyên ≤15, phần thập phân ≤5` (đồng bộ CMR_05 C05b) | `Pending` |
| `UC101-106_TamNgungChamDutDTNN_audited_v5.md` L204 | Nút Lưu nháp | [CROSS_UC_PARITY_CONFLICT] "Luôn Enabled" vs CF_01 dirty-check ở UC329-334 | `Luôn Enabled` | `Disabled khi form chưa dirty, Enabled khi form dirty (CF_01, CMR_14)` | `Pending` |
| `UC101-106_TamNgungChamDutDTNN_audited_v5.md` L205 | Nút Nộp báo cáo | [CROSS_UC_PARITY_CONFLICT] "Luôn Enabled" vs CF_01 dirty-check | `Luôn Enabled` | `Disabled khi form chưa dirty, Enabled khi form dirty (CF_01, CMR_14)` | `Pending` |
| `UC101-106_TamNgungChamDutDTNN_audited_v5.md` L167 | Toast Empty-table | [CMR_CONFLICT] Dấu chấm cuối Toast message | `"Vui lòng nhập ít nhất 1 dòng dữ liệu."` | `"Vui lòng nhập ít nhất 1 dòng dữ liệu"` (bỏ `.`) | `Pending` |
| `UC011-034_bo-ho-so-xuc-tien-dau-tu_audited_20260514_v1.md` L379 | CMR_05 note — Error message | [CMR_CONFLICT] Dấu chấm cuối message | `"Ký tự không hợp lệ..." / "Sai định dạng số."` | `"Sai định dạng số"` (bỏ `.`) | `Pending` |
| `UC185-190_BaoCaoNamDTRNN_audited_20260511_v2.md` L247 | Changelog — Required error fix | [INTRA_DOC_CONFLICT] Changelog ghi fix nhưng v1 chưa cập nhật | `Sửa "Trường bắt buộc." → "Vui lòng nhập [tên trường]" (không dấu `.`)` | Bản v1 cần apply fix này | `Pending` |

---

## SELF-AUDIT EVIDENCE TABLE

| # | Mục kiểm tra | Chi tiết | Kết quả | Ghi chú |
|---|---|---|---|---|
| SA-01 | File coverage | Quét toàn bộ 55 thư mục UC. Skip: 0 file (loại trừ file question-backlog, audited cũ). | ✅ | Sử dụng 4 grep song song trên pattern khác nhau |
| SA-02 | Sibling UC parity | Đã diff: UC329-334_v2 ↔ v3 (decimal precision 1dp vs 5dp), UC299-304_v4 ↔ v5 (max 500 vs 255, error msg), UC215-220_v1 ↔ v2 (max 50 vs 255) | ✅ | Phát hiện 3 cặp intra-UC conflict |
| SA-03 | Intra-doc (Body↔AC) | Cross-check: UC335-340 (BR11 vs AC-12), UC191-196 (body vs AC-04), UC185-190 (body vs AC-04), UC185-190 (v1 vs v2 changelog) | ✅ | 4 INTRA_DOC_CONFLICT phát hiện |
| SA-04 | Error message exact-match | Exact-diff: "Trường bắt buộc" (21 file vi phạm), "Không tìm thấy kết quả" (16 file vi phạm), "Sai định dạng số." trailing dot (4 file vi phạm) | ✅ | Tổng 41 dòng vi phạm exact string |
| SA-05 | Optional field sweep | Đã check: Trường Lý do (UC367-372: 400 vs 3000 ký tự), trường Đề xuất/Kiến nghị (max 1000 — OK), Ghi chú (max 500 — OK) | ✅ | 1 vi phạm max length optional field |
| SA-06 | Decimal precision sweep | Đã diff: 5dp (UC113-UC149 nhóm tài chính), 2dp (UC155, UC215, UC185, UC353), 1dp (UC329-334_v2 — lỗi) | ✅ | UC329-334_v2 L248 dùng 1dp thay vì 5dp |
| SA-07 | Button State sweep | Đã check: UC101-106 "Luôn Enabled" vi phạm CF_01 dirty-check so với UC329-334 | ✅ | 2 dòng vi phạm |
