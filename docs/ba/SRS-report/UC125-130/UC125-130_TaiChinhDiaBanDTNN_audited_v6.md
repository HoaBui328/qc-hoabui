# UC Readiness Review — UC125-130 (Tài chính theo địa bàn - Mẫu A.IV.9a)
**Functional / Black-box Test Readiness Template v3 — Re-audit v6**

**Tài liệu:** UC125-130_TaiChinhDiaBanDTNN.md (phiên bản 1.7)
**Ngày tạo:** 2026-05-22
**Tác giả audit:** QC Auditor Agent — Re-audit v6
**Phiên bản report:** v6 (Full re-audit aligned with SRS v1.7 — Fixed 34 Rows, Editable Mode B, Last Write Wins, Sort)

---

## Feature Brief

Chức năng "Báo cáo tổng hợp tình hình tài chính và nộp ngân sách của TCKT có vốn ĐTNN năm theo địa bàn tỉnh/TP" (Mẫu A.IV.9a) thuộc phân hệ Quản lý ĐTNN vào VN. Báo cáo định kỳ năm, dạng eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới, 5 cột số liệu (C3–C7) hỗ trợ auto-fill từ API TMS (Hệ thống Quản lý Thuế).

**Đặc điểm chính (SRS v1.7):**
- Grid **cố định 34 dòng** — không thêm/xóa dòng. STT + Tỉnh/TP Disabled.
- 5 cột số liệu: Thu XNK, Thu nội địa, Thu dầu thô (đơn vị triệu VNĐ, **tối đa 5 chữ số thập phân**), Số DN Lỗ, Số DN Lãi (integer).
- **Mode A/B auto-detect** (không có toggle UI): API OK → Mode B (auto-fill, **tất cả vẫn Editable** — Exception CMR_12); API fail/timeout → Mode A (toàn bộ Enabled) + Toast T05.
- Retry 3 lần × 5 giây trước khi chuyển Mode A.
- Dòng Tổng = SUM real-time (Disabled).
- Cross-validation **DN Lãi + DN Lỗ ≠ tổng DN FDI** → Warning only (không chặn nộp).
- **9a và 9b (UC131-136) độc lập hoàn toàn** — 9a lấy từ API TMS, 9b lấy từ API Cục Thuế, không tổng hợp qua lại.
- Import .xlsx max 10MB, **validate đúng 34 dòng** (CF_02 Case 2).
- **Last Write Wins** cho concurrent edit — thao tác sau ghi đè, cả 2 ghi Lifecycle Log.
- **Sort** C3-C7 với mặc định C7 Descending. Sort persist server-side.
- Quy trình 3 bước: CMCĐT_BCTK_09.

**Đối tượng sử dụng:** Cục Thuế / Vụ Tài chính (Bộ Tài chính) (Admin site).
**Cơ quan nhận:** Cục Đầu tư nước ngoài, Vụ Ngân sách Nhà nước (Bộ Tài chính).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| **90.0 / 100** | **CONDITIONALLY READY** |

Raw: 99/110 → Final: round((99/110)×100, 1) = **90.0/100**.

**Lý do:** SRS v1.7 đã hoàn thiện đáng kể: Fixed 34 Rows rõ ràng, Mode B Editable với Exception CMR_12, Sort persist, validate import 34 dòng, Last Write Wins, Notification content cụ thể, validate Lưu nháp CF_01 Case 2, Năm báo cáo Disabled. Còn lại gap minor về design images không đọc được full resolution và NFR browser/WCAG.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC125-130 | Báo cáo tổng hợp tài chính ĐTNN theo địa bàn - Mẫu A.IV.9a | v1.7 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | (Pending) | 2026-04-24 | 2026-05-21 |

---
## 1. Objective & Scope

### 1.1 Objective
Hỗ trợ Cục Thuế / Vụ Tài chính (Bộ Tài chính) nộp báo cáo tổng hợp trực tuyến về tình hình tài chính và nộp ngân sách của các tổ chức kinh tế có vốn ĐTNN, phân theo 34 tỉnh/TP (danh mục hành chính sáp nhập mới). Làm căn cứ quản lý thuế và nộp ngân sách theo địa bàn cho Cục ĐTNN.

### 1.2 In Scope
- UC125: Lập báo cáo mới (Mode A - thủ công).
- UC126: Lập báo cáo mới (Mode B - auto-fill từ API TMS).
- UC127: Nộp báo cáo.
- UC128: Chỉnh sửa báo cáo.
- UC129: Xem chi tiết / Xem vòng đời / In / Xuất báo cáo.
- UC130: Xóa báo cáo.
- Xem danh sách báo cáo (lọc, tìm kiếm, nhóm theo kỳ hạn năm).
- Nhập từ file Excel (CF_02 Case 2, validate 34 dòng).

### 1.3 Out of Scope
- Không cho phép nộp báo cáo trễ hạn.
- Duyệt báo cáo (UC riêng biệt).
- Tổng hợp dữ liệu từ UC131-136 (9a/9b độc lập hoàn toàn).
- Quản lý master data 34 tỉnh/TP (thuộc hệ thống danh mục).

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cục Thuế / Vụ Tài chính (Bộ Tài chính) | Primary | Lập, sửa, nộp, xóa báo cáo. Xem danh sách, xem chi tiết, in, xuất báo cáo. Không áp dụng CMR_01/CMR_02 (dành cho NĐT/TCKT). |
| Hệ thống TMS (Tax Management System) | System | Cung cấp dữ liệu auto-fill cho 5 cột số liệu qua API JSON/REST. Group By tỉnh/TP từ DN FDI. |
| Cục Đầu tư nước ngoài / Vụ NSNN (BTC) | Secondary | Cơ quan nhận báo cáo. Nhận Notification khi báo cáo được nộp thành công. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Cục Thuế / Vụ Tài chính (Bộ Tài chính).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn" (CMR_04).
- Danh mục 34 tỉnh/TP theo danh mục hành chính sáp nhập mới đã được cấu hình trong master data.
- API TMS khả dụng (hoặc fallback Mode A nếu API fail).

### 3.2 Postconditions

| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập báo cáo + Lưu nháp | Bản ghi trạng thái "Lưu nháp" xuất hiện trong danh sách. Toast T01: Tiêu đề "Thành công", Nội dung "Đã lập báo cáo thành công" |
| Nộp báo cáo thành công | Trạng thái → "Chờ duyệt" (quy trình 3 bước, CMR_03). Notification gửi Cục ĐTNN: "Báo cáo [Mã báo cáo] đã được nộp bởi [Tên đơn vị lập] cho kỳ [Năm YYYY]". Toast T02 |
| Chỉnh sửa + Lưu | Trạng thái bảo toàn. Toast T03. Audit log (Lifecycle Log) |
| Xóa báo cáo | Bản ghi bị xóa khỏi danh sách. Toast T08: Tiêu đề "Thành công", Nội dung "Xóa báo cáo thành công" |
| Mọi thao tác | Ghi nhận Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CF_06 |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC125-130.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Enum values | Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|------------|--------|
| 1 | Bộ lọc | Năm báo cáo | Yearpicker | No | Năm hiện tại | — | Lọc ngay. CMR_07. Enable toàn bộ năm; năm không có data → Empty State. | SRS UC125-130.1 |
| 2 | Bộ lọc | Trạng thái kỳ hạn | Multiple-selection Dropdown | No | Tất cả | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04, CMR_07, CMR_16. | SRS UC125-130.1 |
| 3 | Bộ lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Tất cả | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03, CMR_07, CMR_16. | SRS UC125-130.1 |
| 4 | Bộ lọc | Mã báo cáo | Search bar | No | Null | — | Placeholder "Tìm kiếm nhanh theo mã báo cáo". CMR_06. | SRS UC125-130.1 |
| 5 | Kỳ hạn Header | Kỳ hạn báo cáo | Label | — | — | — | "Năm YYYY". CMR_08. | SRS UC125-130.1 |
| 6 | Kỳ hạn Header | Trạng thái kỳ | Label/Badge | — | — | CMR_04 | — | SRS UC125-130.1 |
| 7 | Kỳ hạn Header | Lập báo cáo | Button | — | — | — | Chỉ visible khi kỳ "Trong thời hạn". CF_01, CMR_04. | SRS UC125-130.1 |
| 8 | Kỳ hạn Header | Nhập từ file | Button | — | — | — | Chỉ visible khi kỳ "Trong thời hạn". CF_02 Case 2, CMR_04. | SRS UC125-130.1 |
| 9 | Bảng BC | Mã báo cáo | Label | — | — | — | CMR_09: FDI_AIV9A_[ID]. | SRS UC125-130.1 |
| 10 | Bảng BC | Địa bàn | Label | — | — | — | Tỉnh/TP của cơ quan lập. | SRS UC125-130.1 |
| 11 | Bảng BC | Ngày cập nhật | Label | — | — | — | dd/MM/yyyy HH:mm. | SRS UC125-130.1 |
| 12 | Bảng BC | Trạng thái báo cáo | Label | — | — | CMR_03 | — | SRS UC125-130.1 |
| 13 | Bảng BC | Hành động | Button group | — | — | — | Nộp/Chỉnh sửa/Xem chi tiết/Xem vòng đời/In/Xuất báo cáo/Xóa. UC125-130.3. | SRS UC125-130.1 |

### 4.2 Màn hình Lập báo cáo (UC125-130.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Constraint | Source |
|---|------------------|------------------|------|----------|---------|------------|--------|
| 14 | Header | Năm báo cáo | Yearpicker | Yes | Năm từ context kỳ hạn | **Disabled** — không cho sửa. Truyền từ context kỳ hạn đang mở tại màn danh sách. CMR_05. | SRS UC125-130.2 |
| 15 | Cột (1) | STT | Integer (Auto) | — | 1–34 | **Disabled**. Tự đánh số 1–34. | SRS UC125-130.2 |
| 16 | Cột (2) | Tỉnh/Thành phố | Label | — | Master data | **Disabled**. 34 tỉnh/TP theo danh mục hành chính sáp nhập mới, sắp xếp theo mã đơn vị hành chính. | SRS UC125-130.2 |
| 17 | Cột (3) | Nộp ngân sách (triệu VNĐ) - Thu từ xuất, nhập khẩu | Decimal | Yes | Null / Auto-fill API | Tối đa 5 chữ số thập phân. ≥ 0. Mode B: Auto-fill, vẫn **Editable**. CMR_05. | SRS UC125-130.2 |
| 18 | Cột (4) | Nộp ngân sách (triệu VNĐ) - Thu nội địa | Decimal | Yes | Null / Auto-fill API | Tối đa 5 chữ số thập phân. ≥ 0. Mode B: Auto-fill, vẫn **Editable**. CMR_05. | SRS UC125-130.2 |
| 19 | Cột (5) | Nộp ngân sách (triệu VNĐ) - Thu từ dầu thô | Decimal | Yes | Null / Auto-fill API | Tối đa 5 chữ số thập phân. ≥ 0. Mode B: Auto-fill, vẫn **Editable**. CMR_05. | SRS UC125-130.2 |
| 20 | Cột (6) | Số doanh nghiệp — Lỗ | Integer | Yes | Null / Auto-fill API | Integer ≥ 0. Mode B: Auto-fill, vẫn **Editable**. CMR_05. | SRS UC125-130.2 |
| 21 | Cột (7) | Số doanh nghiệp — Lãi | Integer | Yes | Null / Auto-fill API | Integer ≥ 0. Mode B: Auto-fill, vẫn **Editable**. CMR_05. | SRS UC125-130.2 |
| 22 | Dòng Tổng | Tổng — Cột (3) | Auto-calc | — | SUM 34 dòng | **Disabled**. Tối đa 5dp. Real-time. | SRS UC125-130.2 |
| 23 | Dòng Tổng | Tổng — Cột (4) | Auto-calc | — | SUM 34 dòng | **Disabled**. Tối đa 5dp. Real-time. | SRS UC125-130.2 |
| 24 | Dòng Tổng | Tổng — Cột (5) | Auto-calc | — | SUM 34 dòng | **Disabled**. Tối đa 5dp. Real-time. | SRS UC125-130.2 |
| 25 | Dòng Tổng | Tổng — Cột (6) | Auto-calc | — | SUM 34 dòng | **Disabled**. Integer. Real-time. | SRS UC125-130.2 |
| 26 | Dòng Tổng | Tổng — Cột (7) | Auto-calc | — | SUM 34 dòng | **Disabled**. Integer. Real-time. | SRS UC125-130.2 |
| 27 | Footer | Nơi lập báo cáo | Text/Label (Auto) | — | Tên tỉnh/TP trụ sở cơ quan đăng nhập | **Disabled**. Không cho sửa. | SRS UC125-130.2 |
| 28 | Footer | Ngày, tháng, năm | Date/Label (Auto) | — | Current System Date | **Disabled**. dd/MM/yyyy. Không cho sửa. | SRS UC125-130.2 |
| 29 | Actions | Hủy | Button | — | — | CF_01 (Xử lý nút [Hủy]). Dirty check CMR_14. | SRS UC125-130.2 |
| 30 | Actions | Xem trước | Button | — | — | CF_07.1. Disabled khi chưa Lưu nháp lần nào. | SRS UC125-130.2 |
| 31 | Actions | Lưu nháp | Button | — | — | CF_01 (Xử lý nút [Lưu nháp]). Validate CF_01 Case 2. | SRS UC125-130.2 |
| 32 | Actions | Nộp báo cáo | Button | — | — | CF_01 (Xử lý nút [Nộp báo cáo]). Validate C3-C7 ≥ 0. | SRS UC125-130.2 |
| 33 | Sort Header | Icon Sort C3, C4, C5, C6, C7 | Icon Button | — | C7 Descending | Toggle Ascending/Descending. Dòng Tổng luôn ở cuối. Sort persist server-side. | SRS UC125-130.2 |

### 4.3 Tác vụ bổ trợ (UC125-130.3)

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
|---|-----|------|-------------------|------------|-------|
| 34 | Nộp | Button | Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | CF_09. CF_01 (Xử lý nút [Nộp báo cáo]). Disabled khi YCCS + chưa chỉnh sửa (CMR_14). |
| 35 | Chỉnh sửa | Button | Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | CF_03. |
| 36 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | CF_07. |
| 37 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | CF_06. |
| 38 | In | Button | Tất cả trạng thái | Tất cả người dùng | CF_05. |
| 39 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | CF_04. Excel (.xlsx). |
| 40 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | CF_08. |

---
## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Key Behavior |
|--------------------|---------------|--------------|
| STT (Cột 1) | Disabled, auto 1–34 | Hệ thống đánh số cố định. |
| Tỉnh/TP (Cột 2) | Disabled, master data | 34 dòng cố định theo danh mục hành chính sáp nhập mới, sắp xếp theo mã đơn vị hành chính. |
| C3–C7 (Mode B) | **Editable** (Exception CMR_12) | Auto-fill từ API TMS, user vẫn có thể hiệu chỉnh. User chịu trách nhiệm cuối cùng về tính chính xác. |
| C3–C7 (Mode A) | Enabled toàn bộ | Kích hoạt khi API TMS không khả dụng (sau retry 3x5s). Cột Tỉnh/TP điền sẵn, cột số liệu trống + placeholder CMR_05. |
| Dòng Tổng | Disabled, SUM real-time | Cập nhật ngay khi thay đổi ô nào. C3-C5: tối đa 5dp. C6-C7: Integer. Luôn ở cuối bảng (không tham gia sort). |
| Footer | Disabled, auto-fill | Nơi lập theo trụ sở cơ quan đăng nhập, ngày theo Current System Date. |
| Sort Icons (C3-C7) | Toggle Asc/Desc | Mặc định C7 Descending (max→min). Sort persist server-side, restore khi mở CF_03/CF_07. Mode B auto-sort theo default trước render. |
| Nút Lưu nháp | Enabled (trạng thái Lưu nháp) / Disabled khi YCCS + chưa dirty | Validate CF_01 Case 2: ít nhất 1 ô số liệu phải có dữ liệu. Toast T01 (Lập mới) / T03 (Chỉnh sửa). Giữ nguyên màn hình. |
| Nút Nộp báo cáo | Enabled (trạng thái Lưu nháp) / Disabled khi YCCS + chưa dirty | Validate C3–C7 ≥ 0, tối đa 5dp (C3-C5), integer (C6-C7). DN Lãi+Lỗ warning. Popup xác nhận + checkbox. Toast T02. |
| Nút Xem trước | Disabled khi chưa Lưu nháp lần nào / Enabled sau khi bản ghi tồn tại | CF_07.1. Popup PDF Preview. |
| Nút Hủy | Luôn Enabled | Dirty check CMR_14. Popup cảnh báo nếu form dirty. |
| Năm báo cáo | Disabled | Truyền từ context kỳ hạn đang mở tại màn danh sách. Không cho sửa. |

**Cơ chế Mode A/B (Auto-detect):**
- Mở form → health-check API TMS.
- API OK → **Mode B**: auto-fill dữ liệu vào các dòng tương ứng, **tất cả vẫn Editable** (Exception CMR_12).
- API Fail/Timeout → Retry 3 lần × 5 giây → **Mode A**: Toast T05 (Tiêu đề: "Lỗi hệ thống", Nội dung: "Không thể kết nối đến hệ thống. Vui lòng thử lại sau.") + Enable toàn bộ.
- **Không có toggle/switch trên UI.**
- Tỉnh/TP không có dữ liệu từ API → cột số liệu để trống, user tự nhập nếu cần.

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Xem danh sách (UC125-130.1)
1. Truy cập: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Mẫu A.IV.9a.
2. Danh sách nhóm theo kỳ hạn năm, mặc định collapse, sắp xếp giảm dần (CMR_10).
3. Bộ lọc: Năm (Yearpicker), Trạng thái kỳ hạn, Trạng thái báo cáo, Mã báo cáo (CMR_07 hiển thị ngay, CMR_16 mặc định "Tất cả").
4. Nút [Lập báo cáo] + [Nhập từ file] chỉ visible khi kỳ "Trong thời hạn" (CMR_04, CF_01).

### 6.2 Lập BC Mode A - Thủ công (UC125)
1. Mở form. API TMS fail (sau retry 3x5s) → Mode A. Toast T05.
2. Bảng 34 dòng cố định. Cột Tỉnh/TP điền sẵn (Disabled) theo danh mục sáp nhập mới.
3. Các cột số liệu (3)-(7) hiển thị trống, placeholder theo CMR_05.
4. Người dùng nhập trực tiếp 5 cột số liệu cho từng dòng.
5. Dòng Tổng SUM real-time. Footer auto.
6. Validate Nộp: C3–C7 ≥ 0. C3-C5: tối đa 5dp. C6-C7: integer.

### 6.3 Lập BC Mode B - API TMS (UC126)
1. Mở form. API TMS OK → Mode B.
2. API rà quét DN FDI → Group By tỉnh/TP → Tính toán cột (3)-(7). Auto-fill vào dòng tương ứng.
3. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh giá trị sau khi API điền (Exception CMR_12).
4. Tỉnh/TP không có dữ liệu từ API → cột số liệu để trống, user tự nhập nếu cần.
5. Retry: API lỗi tạm thời → retry 3 lần × 5 giây. Sau 3 lần fail → Toast T05 + chuyển Mode A.
6. Hệ thống auto-sort theo default sort (C7 Descending) trước khi render.

### 6.4 Nộp (UC127)
1. Validate C3–C7 ≥ 0 trên 34 dòng. C3-C5: tối đa 5dp. C6-C7: integer.
2. **DN Lãi+Lỗ Warning:** Nếu SUM C6 + SUM C7 ≠ tổng DN FDI (nếu có dữ liệu tham chiếu) → Yellow banner warning: "Tổng số DN Lãi + Lỗ không bằng tổng số DN FDI. Vui lòng kiểm tra." **Không chặn nộp**.
3. Popup xác nhận (CF_01): Tiêu đề "Bạn có chắc muốn nộp?" + checkbox cam kết.
4. Trạng thái → "Chờ duyệt" (quy trình 3 bước, CMR_03). Notification gửi Cục ĐTNN: "Báo cáo [Mã báo cáo] đã được nộp bởi [Tên đơn vị lập] cho kỳ [Năm YYYY]". Toast T02.

### 6.5 Chỉnh sửa (UC128)
- Mở form với data hiện tại (CF_03). Restore sort order đã lưu.
- Thay đổi C3–C7. Lưu nháp / Nộp.
- Trạng thái "YCCS": Nút [Lưu nháp] và [Nộp] Disabled khi chưa dirty. Enable ngay khi form dirty (CMR_14).
- Lưu nháp: trạng thái bảo toàn (không chuyển về "Lưu nháp" nếu đang YCCS). Toast T03. Giữ nguyên màn hình.

### 6.6 Xem/In/Xuất báo cáo (UC129) — CF_04–CF_07
- Xem chi tiết: CF_07. Full-page read-only. Restore sort order.
- Xem trước: CF_07.1. Popup PDF Preview.
- In: CF_05. Print Preview PDF → hộp thoại in trình duyệt.
- Xuất báo cáo: CF_04. **Excel (.xlsx)** template Mẫu A.IV.9a, 34 dòng + tổng.

### 6.7 Xóa (UC130) — CF_08
- Chỉ Lưu nháp **VÀ** chưa từng nộp. Popup xác nhận: "Bạn có chắc chắn muốn xóa báo cáo này?" Toast T08.

### 6.8 Nhập từ file — CF_02 Case 2
- File .xlsx only, max 10MB.
- Template: 34 dòng tương ứng 34 tỉnh/TP (cột Tỉnh/TP pre-filled, Disabled). Người dùng chỉ điền 5 cột số liệu.
- **Validate số dòng:** File upload phải có đúng 34 dòng dữ liệu. Nếu khác 34 → Alert: "Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải."
- **Mapping logic:** Map theo cột Tỉnh/TP (khớp tên). Nếu không khớp → Alert: "Dữ liệu không khớp danh mục tỉnh/thành phố. Vui lòng kiểm tra lại."
- Upload thành công → đóng popup, chuyển đến màn hình Tạo mới. Tất cả trường Enabled.

### 6.9 Validate Lưu nháp — CF_01 Case 2
- Báo cáo KHÔNG CÓ Phạm vi dữ liệu nguồn input → bắt buộc ít nhất 1 ô số liệu (C3-C7) phải có dữ liệu.
- Nếu tất cả ô trống → Toast T07: Tiêu đề "Lưu nháp không thành công", Nội dung "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp".

---

## 7. Functional Integration Analysis

### 7.1 Tích hợp với UC131-136 (Mẫu 9b) — **ĐỘC LẬP**

9a và 9b là **hai báo cáo hoàn toàn độc lập**:
- 9a (UC125-130): nguồn dữ liệu = **API TMS**.
- 9b (UC131-136): nguồn dữ liệu = **API Cục Thuế**.
- **Không tổng hợp qua lại.** Không có aggregation trigger 9b→9a.

### 7.2 Tích hợp với API TMS

- Nguồn: Kho dữ liệu Báo cáo Tài chính và Hồ sơ nộp thuế từ Hệ thống Quản lý Thuế.
- Format: **JSON/REST API**.
- Retry: **3 lần × 5 giây** trước khi chuyển Mode A.
- Exception CMR_12: Sau API fill, tất cả vẫn Editable (khác rule mặc định CMR_12 Disabled).

### 7.3 Tích hợp CF (Common Functions)

| CF | Function | Apply | Notes |
|----|----------|-------|-------|
| CF_01 | Lập báo cáo | UC125–127 | Lưu nháp (Case 2), Xem trước, Nộp, Hủy |
| CF_02 | Nhập từ file | UC125-130.1 | **Case 2 (không có Phạm vi)**, validate 34 dòng, mapping theo tên tỉnh/TP |
| CF_03 | Chỉnh sửa | UC128 | Lưu nháp / YCCS. Bảo toàn trạng thái. Restore sort. |
| CF_04 | Xuất báo cáo | UC129 | Excel (.xlsx) template |
| CF_05 | In | UC129 | Template Mẫu 9a |
| CF_06 | Xem vòng đời | UC129 | Lifecycle Log. Last Write Wins ghi cả 2 thao tác. |
| CF_07 | Xem chi tiết | UC129 | Full-page read-only. Restore sort. |
| CF_08 | Xóa | UC130 | Lưu nháp + chưa nộp |
| CF_09 | Nộp từ DS | UC127 | Disabled khi YCCS + chưa chỉnh sửa (CMR_14) |

### 7.4 Tích hợp CMR

- CMR_03 (trạng thái BC — quy trình 3 bước)
- CMR_04 (trạng thái kỳ hạn)
- CMR_05 (validate số, placeholder, eForm Grid lỗi viền đỏ + tooltip)
- CMR_06 (search, placeholder "Tìm kiếm nhanh theo mã báo cáo")
- CMR_07 (filter instant, dropdown)
- CMR_08 (kỳ hạn label)
- CMR_09 (mã BC: FDI_AIV9A_[ID])
- CMR_10 (collapse/sort/phân trang)
- CMR_12 (API-sourced fields — **Exception: Editable sau fill**)
- CMR_14 (dirty check, Disable nút khi YCCS)
- CMR_16 (filter dropdown mặc định "Tất cả")
- CMR_18 (Tab Navigation — Tab/Shift+Tab theo thứ tự logic)

---
## 8. Acceptance Criteria

### Từ SRS v1.7 (13 AC):

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC1 | Fixed 34 Rows | Mở form Lập BC | Form render | 34 dòng cố định tương ứng 34 tỉnh/TP theo danh mục sáp nhập mới. Không thêm/xóa dòng. |
| AC2 | Mode Detect | Mở form | Health-check API | API OK → Mode B (auto-fill, Editable). API Fail → Retry 3x5s → Mode A + Toast T05 |
| AC3 | Auto-fill TMS (Mode B) | API TMS OK | Fill data | Auto-fill C3-C7 cho dòng có dữ liệu. **Tất cả vẫn Editable** — user có thể hiệu chỉnh (Exception CMR_12) |
| AC4 | API Fail (Mode A) | API TMS không khả dụng | Sau 3 retry | Toast T05, bảng 34 dòng cột số liệu trống, user tự nhập |
| AC5 | Tỉnh/TP Disabled | Mở form | Render | Cột Tỉnh/TP = Label, Disabled. User không thể sửa tên tỉnh/TP |
| AC6 | SUM Real-time | Thay đổi bất kỳ ô nào | Ô thay đổi | Dòng Tổng cập nhật ngay. C3-C5: tối đa 5dp. C6-C7: Integer |
| AC7 | Validate số dương | Nhập C3–C7 < 0 | Click Nộp | Lỗi viền đỏ + tooltip "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" (CMR_05), chặn nộp |
| AC8 | Decimal precision | C3–C5 | Fill/nhập | Tối đa 5 chữ số thập phân. C6–C7 integer |
| AC9 | DN Lãi+Lỗ Warning | SUM C6 + SUM C7 ≠ tổng DN FDI | Click Nộp | Yellow banner warning: "Tổng số DN Lãi + Lỗ không bằng tổng số DN FDI. Vui lòng kiểm tra." **Không chặn nộp** |
| AC10 | Footer tự động | Mở form | Render | Nơi lập + Ngày lập Disabled, auto-fill |
| AC11 | Sort | Mở form / Chỉnh sửa | Render | Icon sort C3-C7. Mặc định C7 Descending. Dòng Tổng luôn ở cuối. Sort persist server-side, restore khi mở CF_03/CF_07 |
| AC12 | Concurrent Edit (Last Write Wins) | 2 user cùng edit 1 BC | User B save sau A | Thao tác sau ghi đè. Cả 2 ghi Lifecycle Log (CF_06) |
| AC13 | 9a/9b Độc lập | Không có aggregation | N/A | Mẫu 9a và 9b không tổng hợp qua lại |

---

## 9. Non-functional Requirements

| NFR # | Category | Requirement | Source |
|-------|----------|-------------|--------|
| NFR-01 | Performance | Tải bảng 34 dòng + auto-fill ≤ 5s. API TMS retry 3 lần × 5 giây. Format: JSON/REST | SRS 3.5 |
| NFR-02 | Security & Audit | Chỉ Cục Thuế / Vụ Tài chính (BTC) có quyền Thêm/Sửa/Nộp. Không áp dụng CMR_01/CMR_02. Lifecycle Log đầy đủ (Actor, Action, Timestamp) | SRS 3.5 |
| NFR-03 | Concurrency | **Last Write Wins** — thao tác sau ghi đè, cả 2 ghi Lifecycle Log (CF_06) | SRS 3.5 |
| NFR-04 | API Format | JSON/REST | SRS 3.5 |
| NFR-05 | Tab Navigation | CMR_18: Tab/Shift+Tab điều hướng giữa các ô trong grid theo thứ tự logic trái→phải, trên→dưới | CMR_18 |
| NFR-06 | eForm Grid Error Display | Lỗi hiển thị viền đỏ quanh ô + tooltip message khi hover (CMR_05, CMR_06) | CMR_05 |
| NFR-07 | Browser Compatibility | (Missing) | — |
| NFR-08 | Accessibility WCAG | (Missing) | — |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
Tất cả câu hỏi từ v3/v5 audit đã được xử lý trong SRS v1.5–v1.7. Không còn open questions.

### 10.2 Dependencies
- API TMS (JSON/REST).
- Common files: CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_08, CMR_09, CMR_10, CMR_12, CMR_14, CMR_16, CMR_18, CF_01–CF_09.
- Master data 34 tỉnh/TP (danh mục hành chính sáp nhập mới).
- Quy trình 3 bước: CMCĐT_BCTK_09.

---

## 11. Change Log

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v1–v5 | 2026-05-07 ~ 2026-05-22 | QC Auditor Agent | Các phiên bản audit trước (dựa trên SRS v1.0–v1.2, nhiều nội dung đã outdated) |
| **v6** | **2026-05-22** | **QC Auditor Agent** | **Full re-audit dựa trên SRS v1.7. Sửa toàn bộ: (1) 63 dòng → 34 dòng, (2) Mode B Disabled → Editable (Exception CMR_12), (3) Optimistic locking → Last Write Wins, (4) Thêm Sort C3-C7 persist, (5) Năm báo cáo Editable → Disabled, (6) Import validate 34 dòng + mapping tên tỉnh/TP, (7) Validate Lưu nháp CF_01 Case 2, (8) Notification content cụ thể, (9) Phân quyền không áp dụng CMR_01/CMR_02, (10) Xóa filter Địa bàn** |

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|----------------|-----|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ Clear |
| 2 | Objective & Scope | 5 | 5/5 | ✅ Clear |
| 3 | Actors & User Roles | 10 | 9/10 | ✅ Clear |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ Clear |
| 5 | UI Object Inventory | 15 | 13/15 | ⚠️ Partial |
| 6 | Object Attributes & Behavior | 20 | 19/20 | ✅ Clear |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ Clear |
| 8 | Functional Integration | 10 | 10/10 | ✅ Clear |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ Clear |
| 10 | NFR | 5 | 3/5 | ⚠️ Partial |
| **Total** | | **110** | **99/110** | **90.0/100** |

### Verdict: CONDITIONALLY READY

SRS v1.7 đã hoàn thiện đáng kể. Đủ điều kiện cho QC bắt đầu test design.

### Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| G1 | Low | Section 4 UI | Design images "Lập báo cáo.png" và "Xem chi tiết.png" có resolution quá lớn, không verify được pixel-level UI. Cần resize hoặc cung cấp mockup nhỏ hơn | Không thể cross-check UI inventory với visual design | Open |
| G2 | Low | Section 9 NFR | Thiếu Browser Compatibility (NFR-07) và Accessibility WCAG (NFR-08) | Không cover compatibility/accessibility testing | Open |

### What's Good (SRS v1.7)

- **Fixed 34 Rows** rõ ràng — 34 tỉnh/TP theo danh mục sáp nhập mới.
- **Mode B Editable** với Exception CMR_12 — user chịu trách nhiệm cuối cùng.
- **Retry 3 lần × 5 giây** trước khi chuyển Mode A.
- **DN Lãi+Lỗ Warning only**, không chặn nộp.
- **9a/9b độc lập hoàn toàn**.
- **Sort C3-C7** với persist server-side và restore khi mở lại.
- **Import validate đúng 34 dòng** + mapping theo tên tỉnh/TP.
- **Last Write Wins** + Lifecycle Log cho concurrent edit.
- **Notification content cụ thể**: "Báo cáo [Mã] đã được nộp bởi [Đơn vị] cho kỳ [Năm]".
- **Validate Lưu nháp** CF_01 Case 2 (ít nhất 1 ô có data).
- **Năm báo cáo Disabled** — truyền từ context kỳ hạn.
- **Phân quyền rõ ràng** — không áp dụng CMR_01/CMR_02 (cơ quan nhà nước).
- **13 AC** coverage tốt (happy + alternative + exception + warning + sort + concurrent).

### Testability Outlook

**Can test now:**
- Mode A/B detection flow (API OK/fail/timeout/retry).
- Auto-fill logic + Editable sau fill (Exception CMR_12).
- SUM real-time + decimal 5dp.
- Validate C3–C7 ≥ 0 (eForm Grid: viền đỏ + tooltip).
- DN Lãi+Lỗ warning banner.
- Sort C3-C7 toggle + persist + restore.
- Import .xlsx validate 34 dòng + mapping tên tỉnh/TP.
- Last Write Wins (concurrent edit + Lifecycle Log).
- Role-based access (Cục Thuế / Vụ Tài chính BTC).
- 9a/9b độc lập (no aggregation).
- Validate Lưu nháp (ít nhất 1 ô có data).
- Năm báo cáo Disabled.
- Nút Xem trước Disabled/Enabled logic.
- Dirty check + Disable nút khi YCCS (CMR_14).
- Tab Navigation (CMR_18).
- AC1–AC13.

**Cannot test yet:**
- Pixel-level UI visual (design images quá lớn - G1).
- Browser/OS compatibility (thiếu NFR - G2).
- WCAG accessibility (thiếu NFR - G2).

### Summary & Recommendation

UC125-130 SRS v1.7 đạt **90.0/100** — cải thiện đáng kể so với v5 audit (86.4). Các gap critical đã được giải quyết hoàn toàn. Chỉ còn 2 gap minor (G1 design resolution, G2 NFR browser/WCAG).

**Recommendation:** **CONDITIONALLY READY** — proceed với test design. Fix G1–G2 trong phase tiếp theo.

---
*UC Readiness Template v3.0 — Re-audit v6 — 2026-05-22*
