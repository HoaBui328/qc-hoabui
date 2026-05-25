# UC Readiness Review — UC107-112 (Báo cáo tổng hợp tình hình xuất, nhập khẩu - Mẫu A.IV.8a)
**Functional / Black-box Test Readiness Template v4 — CMR Alignment**

| Thuộc tính | Giá trị |
|---|---|
| **Tài liệu nguồn** | UC107-112_BaoCaoTongHopXuatNhapKhau.md (phiên bản 1.1) |
| **Ngày tạo** | 2026-05-22 |
| **Tác giả / Agent** | QC Auditor (CMR Alignment v4) |
| **Phiên bản report** | v4 (CMR Alignment — Textbox max 255, Numeric 15+5, Error format, Tab Navigation CMR_18, Button Luôn Enabled) |

---

## Feature Brief

Chức năng Báo cáo tổng hợp tình hình xuất, nhập khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài (Mẫu A.IV.8a) dành cho Cục Hải quan / Bộ Tài chính. Mẫu 8a là báo cáo **tổng hợp (Aggregation)** từ hai báo cáo nguồn cấp Trung ương: Mẫu 8b (xuất khẩu) và Mẫu 8c (nhập khẩu), thực hiện Group By Tỉnh/TP và SUM giá trị theo 63 địa phương. SRS ver 1.1 đã giải quyết 5 câu hỏi audit (Q1–Q5) về nút thao tác, UI Popup chọn nguồn, AC và điều kiện tiền/hậu kỳ. Re-audit v3 áp dụng scoring caps chuẩn (UI Inventory cap 10/15 do thiếu mockup; NFR cap 3/5 do thiếu Browser Compatibility và WCAG). **v4 (CMR Alignment):** Bổ sung maxlength 255 cho textbox, numeric precision 15+5, chuẩn hóa error messages (bỏ dấu `.`), tham chiếu CMR_18 Tab Navigation, ghi nhận Button "Luôn Enabled".

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **93.6 / 100** | ✅ **READY** |

Raw: 103/110 → Final: round((103/110)×100, 1) = **93.6/100**.

---

## 0. Document Metadata

| UC-ID | Feature Name | SRS Version | Status |
|---|---|---|---|
| UC107-112 | Báo cáo tổng hợp tình hình xuất, nhập khẩu - Mẫu A.IV.8a | v1.1 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-05-05 | 2026-05-07 |

---

## 1. Objective & Scope

### 1.1 Objective
Hỗ trợ cán bộ Cục Hải quan / Bộ Tài chính thực hiện tổng hợp số liệu xuất, nhập khẩu theo 63 tỉnh/thành phố từ các báo cáo nguồn cấp Trung ương (8b, 8c) đã được nộp thành công, nộp báo cáo trực tuyến và theo dõi lịch sử phê duyệt.

### 1.2 In Scope
- Xem danh sách báo cáo tổng hợp A.IV.8a theo năm và trạng thái.
- Lập báo cáo mới bằng cách tổng hợp từ Mẫu 8b và 8c qua Popup chọn nguồn.
- Grid cố định 63 dòng (1 dòng = 1 tỉnh/TP), auto-fill từ tổng hợp, cho phép sửa thủ công.
- Tác vụ bổ trợ: Xem chi tiết, Vòng đời, In, Export, Nộp, Chỉnh sửa, Xóa, Phê duyệt, YC chỉnh sửa.

### 1.3 Out of Scope
- Nộp báo cáo khi đã quá hạn kỳ báo cáo.
- Chức năng duyệt báo cáo (UC riêng biệt).

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Cán bộ Cục Hải quan | Primary | Lập, sửa, nộp báo cáo A.IV.8a |
| Bộ Tài chính (cán bộ) | Primary | Lập, sửa, nộp báo cáo A.IV.8a |
| Lãnh đạo (Cục Hải quan / Bộ Tài chính) | Secondary | Phê duyệt, yêu cầu chỉnh sửa báo cáo |
| Cục Đầu tư nước ngoài (Cục ĐTNN) | Receiver | Nhận báo cáo, nhận Notification khi Nộp thành công |
| Hệ thống báo cáo 8b / 8c | System | Cung cấp dữ liệu nguồn để tổng hợp |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Cục Hải quan.
- Kỳ báo cáo năm tương ứng đang ở trạng thái "Trong thời hạn".

### 3.2 Postconditions
| After completing... | System state |
|---|---|
| Lưu nháp | Báo cáo ở trạng thái "Lưu nháp", lưu vào DB |
| Nộp báo cáo | Trạng thái "Chờ duyệt"; Notification gửi Cục ĐTNN; Audit log ghi nhận |
| Xóa báo cáo | Chỉ với trạng thái "Lưu nháp" chưa từng nộp; Soft-delete; ghi Audit log |
| Phê duyệt | Trạng thái "Đã tiếp nhận" (hoặc tương đương); ghi Audit log |

---

## 4. UI Object Inventory & Mapping

Xem chi tiết trong SRS ver 1.1 Section UC107-112.1 (màn hình danh sách) và UC107-112.2 (form lập báo cáo). Bảng inventory đã đầy đủ với các phần tử:
- **Màn danh sách:** Năm báo cáo (Yearpicker), Trạng thái báo cáo (Multi-select Dropdown), Mã báo cáo (Search bar), Cột bảng gồm: Mã báo cáo, Năm báo cáo, Ngày cập nhật, Trạng thái, Hành động (Button group).
- **Form lập báo cáo:** Năm báo cáo (Yearpicker, required), Nút [Tổng hợp dữ liệu], Grid 63 dòng cố định (STT, Địa phương, Giá trị xuất khẩu USD, Giá trị nhập khẩu USD), Dòng tổng cộng (Tổng xuất khẩu, Tổng nhập khẩu, Calculated), Footer (Nơi lập báo cáo, Ngày tháng năm), Buttons: Lưu nháp / Nộp báo cáo / Hủy.
- **Popup [Chọn báo cáo nguồn]:** 2 tab/danh sách (Mẫu 8b - Xuất khẩu, Mẫu 8c - Nhập khẩu); các cột: Mã báo cáo, Ngày lập, Người lập, Trạng thái; tính năng tìm kiếm/lọc; Nút [Xác nhận].
- **Action Mapping Buttons:** Chỉnh sửa, Nộp, Xóa, Phê duyệt, YC chỉnh sửa, Xem chi tiết, In, Export, Vòng đời (đầy đủ điều kiện hiển thị và phân quyền).

**Note:** SRS text-only, không có mockup đính kèm → không thể verify 100% UI elements visual. Đây là gap cấu trúc (UI Inventory cap 10/15).

---

## 5. Object Attributes & Behavior Definition

Hành vi chi tiết đã được SRS ver 1.1 mô tả đầy đủ:

- **Grid 63 dòng:** STT tự động, Địa phương Disabled (load từ CSDL hành chính), Giá trị xuất/nhập khẩu Decimal ≥ 0, auto-fill sau tổng hợp, cho phép sửa thủ công.
- **Dòng tổng cộng:** Calculated real-time = SUM cột tương ứng, Disabled.
- **Footer:** Nơi lập báo cáo load từ Profile (Disabled), Ngày tháng năm = Current System Date (Disabled).
- **Popup chọn nguồn:** Required chọn đúng 1 bản ghi ở mỗi danh sách (8b và 8c); Nút [Xác nhận] Disabled nếu chưa chọn đủ.
- **Logic tổng hợp:** Group By Tỉnh/TP; SUM Tổng tiền xuất khẩu (8b) theo tỉnh; SUM Tổng tiền nhập khẩu (8c) theo tỉnh.
- **Nguồn dữ liệu mặc định:** Các bản ghi 8b/8c ở trạng thái [Đã tiếp nhận] trong năm báo cáo đã chọn.
- **Action Mapping:** Phân quyền Người lập / Lãnh đạo rõ ràng theo trạng thái bản ghi.

### 5.1 Quy tắc Maxlength & Validation (CMR Alignment)

| Loại trường | Maxlength | Error khi vượt quá |
|---|---|---|
| Textbox | 255 ký tự | "[Tên trường] không được vượt quá 255 ký tự!" |
| Textarea | 3000 ký tự | "[Tên trường] không được vượt quá 3000 ký tự!" |
| Trường số (Numeric) | 21 ký tự (15 nguyên + 1 `.` + 5 thập phân) | "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |
| Search box | 255 ký tự | "[Tên trường] không được vượt quá 255 ký tự!" |

**Áp dụng cụ thể cho UC107-112:**

| Field | Type | Maxlength | Required Error | Maxlength Error |
|---|---|---|---|---|
| Giá trị xuất khẩu (USD) | Numeric (Decimal ≥ 0) | 21 (15+1+5) | "Vui lòng nhập Giá trị xuất khẩu" | "Giá trị xuất khẩu chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |
| Giá trị nhập khẩu (USD) | Numeric (Decimal ≥ 0) | 21 (15+1+5) | "Vui lòng nhập Giá trị nhập khẩu" | "Giá trị nhập khẩu chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |
| Năm báo cáo | Yearpicker | — | "Vui lòng chọn Năm báo cáo" | — |
| Mã báo cáo (search) | Search box | 255 | — | "Mã báo cáo không được vượt quá 255 ký tự!" |

> **Lưu ý:** Tất cả error message KHÔNG có dấu `.` ở cuối câu (theo CMR chuẩn).

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Xem Danh Sách (UC107-112.1)

**A. Workflows:**
1. Truy cập: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Mẫu A.IV.8a.
2. Lọc theo Năm báo cáo (Yearpicker, mặc định năm hiện tại).
3. Lọc theo Trạng thái báo cáo (multi-select, kết quả ngay lập tức).
4. Tìm kiếm theo Mã báo cáo (search bar, kết quả ngay lập tức; "Không tìm thấy kết quả" nếu không có).
5. Sắp xếp giảm dần theo năm. Phân trang 10 bản ghi/trang (CMR_10).

**B. Business Rules:**
| Field | Constraint |
|---|---|
| Năm báo cáo (filter) | Mặc định năm hiện tại (CMR_07) |
| Trạng thái báo cáo | Multi-select: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa |
| Mã báo cáo (search) | Pattern: DTNN_A4_8A_[ID]; Placeholder "Nhập dữ liệu" |

### 6.2 Lập Báo Cáo - Tổng hợp dữ liệu (UC107-112.2)

**A. Workflows:**
1. Từ màn danh sách → Nhấn [Lập báo cáo].
2. Chọn Năm báo cáo (required).
3. Nhấn [Tổng hợp dữ liệu] → Popup [Chọn báo cáo nguồn] hiển thị.
4. Popup: Tab 8b (xuất khẩu) + Tab 8c (nhập khẩu); chọn đúng 1 bản ghi mỗi bên.
5. Nhấn [Xác nhận] → Hệ thống tính toán Group By + SUM → Đổ vào Grid 63 dòng.
6. User có thể sửa thủ công các giá trị sau tổng hợp.
7. Nhấn [Lưu nháp] hoặc [Nộp báo cáo].

**B. Business Rules & Validations:**
| Field | Required | Validate | Error/Note |
|---|---|---|---|
| Năm báo cáo | Yes | Yearpicker | CMR_05 |
| Giá trị xuất khẩu (USD) | Yes | Decimal ≥ 0 | CMR_05 |
| Giá trị nhập khẩu (USD) | Yes | Decimal ≥ 0 | CMR_05 |
| Nộp báo cáo | — | Validate các trường bắt buộc | Chuyển trạng thái "Chờ duyệt" nếu pass |

**C. UI/UX Feedback:**
- Popup [Xác nhận]: Disabled nếu chưa chọn đủ 1 bản ghi mỗi danh sách, hoặc hiển thị lỗi khi nhấn.
- Kết quả lọc/tìm kiếm: Hiển thị ngay lập tức (CMR_07).
- Xóa: Soft-delete, ghi Audit log.

### 6.3 Các Tác Vụ Bổ Trợ & Phê Duyệt (UC107-112.3)

| Tác vụ | Điều kiện hiển thị | Phân quyền | Tham chiếu |
|---|---|---|---|
| Chỉnh sửa | Lưu nháp, YC chỉnh sửa | Người lập | CF_03 |
| Nộp | Lưu nháp, YC chỉnh sửa | Người lập | CF_09 |
| Xóa | Lưu nháp (chưa từng nộp) | Người lập | CF_08 |
| Phê duyệt | Chờ duyệt | Lãnh đạo | CF_01 |
| YC chỉnh sửa | Chờ duyệt | Lãnh đạo | CF_03 |
| Xem chi tiết | Tất cả | Tất cả | CF_07 |
| In | Tất cả | Tất cả | CF_05 |
| Export | Tất cả | Tất cả | CF_04 |
| Vòng đời | Tất cả | Tất cả | CF_06 |

- **Export:** Định dạng Excel theo đúng Mẫu A.IV.8.a (CF_04).
- **In:** Kết xuất PDF và mở hộp thoại in (CF_05).

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---|---|---|
| Nộp báo cáo 8a | Notification gửi Cục ĐTNN; trạng thái "Chờ duyệt" | Danh sách refresh; Audit log |
| Xóa báo cáo | Chỉ Lưu nháp chưa nộp; soft-delete | Audit log ghi nhận |
| Nhấn [Tổng hợp dữ liệu] | Đọc dữ liệu 8b/8c [Đã tiếp nhận]; Group By tỉnh/TP; SUM giá trị | Grid 63 dòng được điền; cho phép sửa thủ công |
| Popup xác nhận nguồn | Required 1 bản ghi 8b + 1 bản ghi 8c | Ngăn tổng hợp nếu thiếu nguồn |
| CSDL hành chính | Load danh mục 63 tỉnh/TP vào Grid | Địa phương Disabled, không sửa |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|---|---|---|---|---|
| AC-01 | Hiển thị Popup nguồn | Đã chọn Năm báo cáo | Nhấn [Tổng hợp dữ liệu] | Popup hiển thị 2 danh sách 8b và 8c với đầy đủ: Mã, Ngày lập, Người lập, Trạng thái |
| AC-02 | Ràng buộc chọn nguồn | Chưa chọn đủ 1 báo cáo mỗi bên | Click [Xác nhận] trên Popup | Nút Disabled hoặc hiển thị thông báo lỗi, không thực hiện tổng hợp |
| AC-03 | Tính toán tổng hợp đúng | Đã chọn đủ 8b + 8c | Nhấn [Xác nhận] | Hệ thống sum dữ liệu theo tỉnh/TP và điền đúng vào cột 5, 6 của Grid |
| AC-04 | Chỉnh sửa sau tổng hợp | Grid đã được auto-fill | User sửa giá trị tại cột 5 hoặc 6 | Hệ thống cho phép sửa; dòng tổng cộng cập nhật real-time |
| AC-05 | Tính tổng cộng | User thay đổi giá trị bất kỳ dòng tỉnh/TP | Nhập/sửa giá trị | Dòng tổng cộng (cột tương ứng) cập nhật chính xác ngay lập tức |
| AC-06 | Nộp báo cáo thành công | Tất cả validate pass (Năm báo cáo, dữ liệu hợp lệ) | Click [Nộp báo cáo] | Trạng thái "Chờ duyệt", Notification gửi Cục ĐTNN |

---

## 9. Non-functional Requirements

| Category | Requirement | Source | Status |
|---|---|---|---|
| Performance | Logic tổng hợp và hiển thị Grid < 5 giây | SRS 3.5 NFR | ✅ Documented |
| Security | Chỉ người dùng có thẩm quyền (Cục Hải quan/Bộ Tài chính) mới thực hiện được | SRS 3.5 NFR | ✅ Documented |
| Audit | Lưu nhật ký thay đổi cho thao tác phê duyệt, chỉnh sửa, xóa báo cáo | SRS 3.5 NFR | ✅ Documented |
| Browser Compatibility | (Thiếu — không ghi rõ Browser/OS support) | — | ⚠️ Missing |
| Accessibility | (Thiếu WCAG — không đề cập) | — | ⚠️ Missing |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
Các câu hỏi từ Backlog v1 và v2 đã resolved (Q1–Q5). Không còn câu hỏi mở từ phía audit.

**Gap mới phát hiện tại re-audit v3:**

| ID | Priority | Ref | Gap | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | Section UC107-112.2 — UI | SRS text-only, không có mockup đính kèm → UI Inventory không thể verify visual layout | Không thể test pixel-level UI; gap cấu trúc | Open |
| G2 | Low | Section 3.5 NFR | Thiếu Browser Compatibility (Chrome/Edge/Firefox phiên bản hỗ trợ) | Không cover compatibility testing | Open |
| G3 | Low | Section 3.5 NFR | Thiếu Accessibility (WCAG 2.1 AA) | Không cover accessibility testing | Open |

### 10.2 Dependencies
- Hệ thống báo cáo Mẫu 8b (Xuất khẩu) và Mẫu 8c (Nhập khẩu).
- CSDL hành chính (danh mục 63 tỉnh/TP).
- Common files: CMR_02, CMR_03, CMR_05, CMR_06, CMR_07, CMR_09, CMR_10, CMR_12, CF_01–CF_09.

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-05-06 | QC Auditor | Initial audit — phát hiện thiếu UI buttons, Popup detail, AC, Pre/Post |
| v2 | 2026-05-06 | QC Auditor | Re-audit sau khi SRS update lên ver 1.1. Cho điểm 110/110 (chưa áp dụng caps) |
| v3 | 2026-05-07 | QC Auditor | Re-audit với scoring caps chuẩn: UI cap 10/15 (thiếu mockup), NFR cap 3/5 (thiếu Browser/WCAG). Raw 103/110 → Final 93.6/100. READY |

---

## Audit Summary

| # | Knowledge Area | Max | Raw Score | Cap | Final Score | Status |
|---|---|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5 | — | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5 | — | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10 | — | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10 | — | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15 | cap 10/15 (không mockup) | 10/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 20 | — | 20/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20 | — | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10 | — | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10 | — | 10/10 | ✅ |
| 10 | NFR | 5 | 5 | cap 3/5 (thiếu Browser/WCAG) | 3/5 | ⚡ |
| **Total** | | **110** | **110** | — | **103/110** | **93.6/100** |

---

## Unified Gap Report

| ID | Priority | Area | Gap Description | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | UI Object Inventory (Area 5) | SRS text-only, không có mockup đính kèm → không thể verify visual layout, spacing, responsive | Không thể test pixel-level UI; không confirm button placement | Open |
| G2 | Low | NFR (Area 10) | Thiếu Browser Compatibility (chưa ghi rõ Chrome/Edge/Firefox phiên bản hỗ trợ) | Không cover cross-browser testing | Open |
| G3 | Low | NFR (Area 10) | Thiếu Accessibility requirements (WCAG 2.1 AA hoặc tương đương) | Không cover accessibility testing | Open |

---

## What's Good

- Kiến trúc Aggregation từ Mẫu 8b + 8c được mô tả rõ ràng và logic Group By / SUM được chỉ định cụ thể.
- Grid cố định 63 dòng (1 dòng = 1 tỉnh/TP) với auto-fill + cho phép sửa thủ công — thiết kế thực tế, dễ test.
- Popup chọn nguồn với Required 1 report mỗi bên — ràng buộc chặt chẽ, ngăn sai sót dữ liệu.
- Action Mapping đầy đủ 9 buttons với điều kiện hiển thị và phân quyền rõ ràng (Người lập / Lãnh đạo).
- 6 AC bao phủ các luồng quan trọng: Popup nguồn, tổng hợp, sửa thủ công, tổng cộng real-time, nộp thành công.
- NFR Performance cụ thể (< 5s), Security và Audit log đều có mặt.
- Soft-delete với Audit log — thiết kế an toàn cho dữ liệu.

---

## Testability Outlook

**Can test now:**
- Luồng tổng hợp dữ liệu từ 2 nguồn 8b và 8c (AC-01, AC-02, AC-03).
- Chỉnh sửa thủ công sau tổng hợp và cập nhật dòng tổng cộng real-time (AC-04, AC-05).
- Nộp báo cáo: validate, chuyển trạng thái, Notification (AC-06).
- Lưu nháp và phục hồi dữ liệu.
- Lọc/tìm kiếm danh sách theo Năm, Trạng thái, Mã báo cáo.
- Action Mapping theo phân quyền Người lập / Lãnh đạo.
- Xóa (soft-delete, Audit log).
- Export Excel đúng mẫu A.IV.8.a.
- In (kết xuất PDF).

**Cannot test yet:**
- Pixel-level UI visual và layout (thiếu mockup — G1).
- Cross-browser / OS compatibility (thiếu NFR — G2).
- WCAG accessibility (thiếu NFR — G3).

---

## Summary & Recommendation

UC107-112 SRS ver 1.1 đạt **93.6/100** (Raw 103/110) sau re-audit v3 với scoring caps chuẩn. Tài liệu đã giải quyết toàn bộ câu hỏi từ Backlog v1 và v2 (Q1–Q5). Logic nghiệp vụ core (Aggregation 8b+8c, Group By tỉnh/TP, Grid 63 dòng, Popup chọn nguồn) được mô tả rõ ràng và đủ để thiết kế test. Các gap còn lại (G1–G3) là minor và không chặn test design.

**Recommendation:** ✅ **READY** — tiến hành thiết kế kịch bản kiểm thử. Fix G1–G3 có thể thực hiện song song.

---
*UC Readiness Template v3.0 — Re-audit v3 — 2026-05-07*
