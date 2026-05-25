# UC Readiness Review — UC227-231: Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)

| Thuộc tính | Giá trị |
|---|---|
| **Ngày audit** | 2026-05-21 |
| **Phiên bản** | v1 |
| **Agent** | BA-audit-SRS-report |
| **Verdict** | ⚠️ CONDITIONALLY READY |
| **Score** | 75.5 / 100 |

---

## Section 0: Feature Identity

| Thuộc tính | Giá trị | Status |
|---|---|---|
| UC ID | UC227-231 | ✅ |
| Tên chức năng | Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2) | ⚡ |
| Phân hệ | Quản lý đầu tư trong nước Việt Nam | ✅ |
| Mẫu biểu | Mẫu A.III.2 | ⚡ |
| Quy tắc sinh mã | DDI_AIII2_[ID] | ⚡ |
| Loại báo cáo | Định kỳ năm | ✅ |
| Giao diện | User site | ✅ |

**Ghi chú:** Theo file `appendices.md` (v2.0), phân hệ DDI có UC227-232 (Quý, mã `DDI_AI3_[ID]`) và UC233-238 (Năm, mã `DDI_AI2_[ID]`). File UC hiện tại dùng dải UC227-231 với mã `DDI_AIII2_[ID]` — không khớp với appendices. Cần BA xác nhận lại dải UC và mã biểu chính xác.

---

## Section 1: Objective & Scope

**Mục tiêu:** Cho phép Tổ chức kinh tế (TCKT) thực hiện dự án lập và nộp báo cáo tình hình thực hiện dự án đầu tư năm theo Mẫu A.III.2 cho phân hệ Đầu tư trong nước.

**Phạm vi:**
- ✅ Xem danh sách báo cáo (UC227-231.1)
- ✅ Lập báo cáo (UC227-231.2)
- ✅ Các tác vụ bổ trợ (UC227-231.3)

**Status:** ✅ Clear — mục tiêu và phạm vi được mô tả rõ ràng.

---

## Section 2: Actors & User Roles

| Actor | Quyền | Tham chiếu |
|---|---|---|
| TCKT phụ trách dự án | Toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo | CMR_01 |
| NĐT thành viên trong dự án | Chỉ Xem (view-only) | CMR_01 |

**Status:** ✅ Clear — phân quyền rõ ràng theo CMR_01 (Case A — ĐTNN/ĐTTN).

---

## Section 3: Preconditions & Postconditions

**Preconditions:**
- ✅ Người dùng đã đăng nhập với vai trò TCKT hoặc NĐT thành viên
- ✅ Kỳ hạn báo cáo ở trạng thái "Trong thời hạn" để tạo mới (CMR_04)
- ✅ Dự án thuộc TCKT đang đăng nhập (CMR_01)

**Postconditions:**
- ✅ Sau khi Lưu nháp: Bản ghi ở trạng thái "Lưu nháp"
- ✅ Sau khi Nộp: Bản ghi chuyển sang "Đã tiếp nhận" (quy trình 2 bước — CMR_03)

**Status:** ✅ Clear

---

## Section 4: UI Object Inventory & Mapping

### UC227-231.1 — Màn hình Danh sách

| # | Tên trường | Kiểu | Section | Status |
|---|---|---|---|---|
| 1 | Năm | Yearpicker | Filter | ✅ |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Filter | ✅ |
| 3 | Dự án | Dropdown/Search | Filter | ✅ |
| 4 | Trạng thái báo cáo | Multiple-selection Dropdown | Filter | ✅ |
| 5 | Mã báo cáo | Search bar | Filter | ✅ |
| 6 | Kỳ hạn báo cáo | Label | Danh sách kỳ | ✅ |
| 7 | Trạng thái kỳ | Label | Danh sách kỳ | ✅ |
| 8 | Lập báo cáo | Button | Danh sách kỳ | ✅ |
| 9 | Nhập từ file | Button | Danh sách kỳ | ✅ |
| 10 | Tên dự án | Label | Danh sách BC | ✅ |
| 11 | Mã báo cáo | Label | Danh sách BC | ✅ |
| 12 | Ngày cập nhật | Label | Danh sách BC | ✅ |
| 13 | Trạng thái báo cáo | Label | Danh sách BC | ✅ |
| 14 | Hành động | Button group | Danh sách BC | ✅ |

### UC227-231.2 — Màn hình Lập Báo Cáo

**Header:**
| # | Tên trường | Kiểu | Status |
|---|---|---|---|
| 1 | Năm báo cáo | Read-only | ✅ |

**Phần A — 13 trường:**
| # | Tên trường | Kiểu | Status |
|---|---|---|---|
| 1 | Tên dự án / Tên Hợp đồng BCC | Dropdown | ✅ |
| 2 | Mã số dự án / Số GCNĐT | Label | ✅ |
| 3 | Ngày cấp GCNĐKĐT | Label | ✅ |
| 4 | Cơ quan cấp GCNĐKĐT | Label | ✅ |
| 5 | Địa điểm thực hiện dự án | Label | ✅ |
| 6 | Tổng vốn đầu tư đăng ký | Label | ✅ |
| 7 | Tên tổ chức kinh tế | Label | ✅ |
| 8 | Mã số DN / MST | Label | ✅ |
| 9 | Ngày cấp lần đầu ĐKKD | Label | ✅ |
| 10 | Cơ quan cấp ĐKKD | Label | ✅ |
| 11 | Địa chỉ liên hệ | Text | ✅ |
| 12 | Số điện thoại | Text | ✅ |
| 13 | Email | Text | ✅ |

**Phần B — eForm Grid (đầy đủ 13 mục chính + Block NĐT):** ✅ Liệt kê chi tiết

**Phần C:**
| # | Tên trường | Kiểu | Status |
|---|---|---|---|
| 1 | Cập nhật khó khăn, vướng mắc và kiến nghị | Textarea | ✅ |

**Buttons:**
| # | Tên | Status |
|---|---|---|
| B1 | Hủy | ✅ |
| B2 | Xem | ✅ |
| B3 | Lưu nháp | ✅ |
| B4 | Nộp báo cáo | ✅ |

### UC227-231.3 — Tác vụ bổ trợ (7 buttons): ✅

**Status:** ✅ Clear — Tất cả UI elements được liệt kê chi tiết, đầy đủ atomic level.

**Lưu ý:** Không có design mockup/wireframe đi kèm nên không thể thực hiện UI Coverage Self-Verification. Đánh giá dựa hoàn toàn trên tài liệu SRS.

---

## Section 5: Object Attributes & Behavior Definition

| Object | System State | Behavior | Status |
|---|---|---|---|
| Năm (Filter) | Enabled, default = năm hiện tại | Chọn → lọc + nhóm danh sách. CMR_07 | ✅ |
| Trạng thái kỳ (Filter) | Enabled | Multi-select, real-time filter. CMR_04, CMR_07, CMR_16 | ✅ |
| Dự án (Filter) | Enabled, default = Tất cả | Chỉ hiển thị dự án thuộc TCKT. CMR_01, CMR_16 | ✅ |
| Trạng thái báo cáo (Filter) | Enabled | Multi-select. CMR_03, CMR_07, CMR_16 | ✅ |
| Mã báo cáo (Search) | Enabled | Tìm theo mã. CMR_06, CMR_09 | ✅ |
| Nút [Lập báo cáo] | Hidden khi Chưa tới hạn/Qua kỳ; Visible khi Trong thời hạn | Mở form lập. CF_01, CMR_18 | ✅ |
| Nút [Nhập từ file] | Hidden khi Chưa tới hạn/Qua kỳ; Visible khi Trong thời hạn | Mở popup import. CF_02 | ✅ |
| Tên dự án (Dropdown A-001) | Enabled | Chọn → auto-fill Phần A. CMR_01, CMR_07, CMR_12, RULE-02 | ✅ |
| Trường API (#2-#10) | Disabled (chờ API) → Disabled (có data) / Enabled (null/lỗi) | CMR_12 | ✅ |
| Trường editable (#11-#13) | Enabled, auto-fill từ API | Cho phép sửa. CMR_06, CMR_12 | ✅ |
| eForm Grid cells (Editable) | Enabled | Nhập số. CMR_05 | ✅ |
| eForm Grid cells (Auto-calc) | Disabled (read-only) | Tính real-time | ✅ |
| eForm Grid cells (Locked) | Disabled | Không nhập | ✅ |
| Block NĐT (Row 1-2) | Disabled (API) | Read-only. CMR_12 | ✅ |
| Block NĐT (Row 4-6) | Enabled | Editable. CMR_05 | ✅ |
| Nút [Hủy] | Enabled | Dirty check → popup CMR_14. CF_01 | ✅ |
| Nút [Xem] | Disabled khi chưa lưu; Enabled sau lưu | PDF Preview. CF_07.1 | ✅ |
| Nút [Lưu nháp] | Enabled | Validate tối thiểu. CF_01 | ✅ |
| Nút [Nộp báo cáo] | Enabled | Full validate + popup xác nhận. CF_01 | ✅ |

**Status:** ✅ Clear — Behavior definition đầy đủ cho tất cả objects.

---

## Section 6: Functional Logic & Workflow Decomposition

### 6.1 Xem Danh sách (UC227-231.1)

**Main Flow:** Truy cập → Hệ thống hiển thị danh sách nhóm theo kỳ hạn năm, collapse mặc định, sắp xếp giảm dần. ✅

**Business Rules:**
- CMR_01: Mỗi TCKT chỉ thấy báo cáo của mình
- CMR_04: Trạng thái kỳ hạn quyết định hiển thị nút
- CMR_08: Nhóm theo kỳ hạn
- CMR_10: Phân trang
- CS_01: Empty state "Kỳ báo cáo này chưa tới hạn..."

**Status:** ✅ Clear

### 6.2 Lập Báo Cáo (UC227-231.2)

**Main Flow:**
1. Nhấn [Lập báo cáo] → Mở form
2. Chọn Dự án (A-001) → API auto-fill Phần A
3. Nhập liệu Phần B (eForm Grid) + Phần C
4. [Lưu nháp] hoặc [Nộp báo cáo]

**Alternative Flows:**
- API lỗi → Toast T05, Enable trường nhập tay (CMR_12) ✅
- Đổi dự án sau khi nhập Phần B → Popup P02 cảnh báo xóa dữ liệu (RULE-02) ✅
- Validate Năm: Năm BC ≥ Năm cấp GCNĐKĐT (RULE-03) ✅

**Exception Flows:**
- Validate số: >= 0 cho hầu hết trường; cho phép âm ở mục 2, 3 ✅
- RULE-01: Dự án VNĐ → đổi label USD sang Triệu VNĐ ✅

**Status:** ✅ Clear

### 6.3 Tác vụ bổ trợ (UC227-231.3)

| Tác vụ | Điều kiện | Tham chiếu | Status |
|---|---|---|---|
| Nộp | Lưu nháp / YC chỉnh sửa | CF_09 | ✅ |
| Chỉnh sửa | Lưu nháp / YC chỉnh sửa | CF_03 | ✅ |
| Xem chi tiết | Tất cả trạng thái | CF_07 | ✅ |
| Xem vòng đời | Tất cả trạng thái | CF_06 | ✅ |
| In | Tất cả trạng thái | CF_05 | ✅ |
| Xuất báo cáo | Tất cả trạng thái | CF_04 | ✅ |
| Xóa | Lưu nháp VÀ chưa từng nộp | CF_08 | ✅ |

**Status:** ✅ Clear

---

## Section 7: Functional Integration Analysis

| Chức năng nguồn | Chức năng đích | Ảnh hưởng | Status |
|---|---|---|---|
| Chọn Dự án (A-001) | Phần A (auto-fill) | API call → fill 12 trường | ✅ |
| Chọn Dự án (A-001) | Phần B (Block NĐT) | API → render blocks NĐT | ✅ |
| Đổi Dự án | Phần B | Xóa trắng toàn bộ (RULE-02) | ✅ |
| Lưu nháp | Danh sách | Bản ghi xuất hiện, trạng thái "Lưu nháp" | ✅ |
| Nộp | Danh sách | Trạng thái → "Đã tiếp nhận" (2 bước) | ✅ |
| RULE-01 (VNĐ) | Phần A + B | Đổi label đơn vị USD → Triệu VNĐ | ✅ |

**Status:** ✅ Clear

---

## Section 8: Acceptance Criteria

### AC-01: Danh sách báo cáo
- **Given** TCKT đăng nhập có dự án
- **When** truy cập màn hình danh sách
- **Then** chỉ hiển thị báo cáo của TCKT đó, nhóm theo năm, collapse mặc định

### AC-02: Lập báo cáo — Auto-fill
- **Given** kỳ hạn "Trong thời hạn"
- **When** nhấn [Lập báo cáo] và chọn Dự án
- **Then** hệ thống gọi API và auto-fill 12 trường Phần A (Disabled)

### AC-03: Lập báo cáo — API lỗi
- **Given** API không phản hồi
- **When** chọn Dự án
- **Then** Toast T05 hiển thị, trường chuyển Enabled cho nhập tay

### AC-04: eForm Grid — Auto-calc
- **Given** người dùng nhập giá trị tại mục 2.a, 2.b, 2.c
- **When** blur khỏi ô
- **Then** mục 2 (Vốn vay) = Σ(2.a + 2.b + 2.c), cập nhật real-time

### AC-05: RULE-01 — Đổi đơn vị
- **Given** dự án được cấp GCNĐKĐT bằng VNĐ
- **When** chọn dự án đó
- **Then** toàn bộ label "USD" đổi sang "Triệu VNĐ", riêng mục VI giữ nguyên "triệu VNĐ"

### AC-06: RULE-02 — Đổi dự án
- **Given** đã nhập liệu Phần B
- **When** đổi dự án tại A-001
- **Then** popup P02 hiển thị; [Tiếp tục] → xóa Phần B; [Hủy] → giữ nguyên

### AC-07: Nộp báo cáo
- **Given** tất cả trường bắt buộc hợp lệ
- **When** nhấn [Nộp báo cáo] → tích checkbox → [Xác nhận]
- **Then** trạng thái → "Đã tiếp nhận", Toast thành công, quay về Danh sách

### AC-08: Xóa báo cáo
- **Given** bản ghi "Lưu nháp" VÀ chưa từng nộp
- **When** nhấn [Xóa] → [Đồng ý]
- **Then** bản ghi bị xóa, Toast T08

**Status:** ⚡ Partial — AC được suy ra từ tài liệu, nhưng source document không có AC tường minh.

---

## Section 9: Non-functional Requirements

| NFR | Status | Ghi chú |
|---|---|---|
| Performance | ⚠️ Missing | Không có yêu cầu về thời gian phản hồi API, load time |
| Security | ⚡ Partial | Phân quyền CMR_01 có, nhưng không có chi tiết về session/token |
| Accessibility | ⚠️ Missing | Không đề cập |
| Compatibility | ⚠️ Missing | Không đề cập browser/device support |
| Tab Navigation | ✅ Clear | CMR_18 |

**Status:** ⚡ Partial

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 4/5 | ⚡ Partial — Mã UC và mã biểu không khớp appendices |
| 2 | Objective & Scope | 5 | 5/5 | ✅ Clear |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ Clear |
| 4 | Preconditions & Postconditions | 10 | 9/10 | ✅ Clear |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | ⚡ Partial — Không có wireframe để cross-verify |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ✅ Clear |
| 7 | Functional Logic & Workflow Decomposition | 20 | 18/20 | ✅ Clear |
| 8 | Functional Integration Analysis | 10 | 9/10 | ✅ Clear |
| 9 | Acceptance Criteria | 10 | 7/10 | ⚡ Partial — Inferred, không có AC tường minh trong source |
| 10 | Non-functional Requirements | 5 | 2/5 | ⚡ Partial |
| **Total** | | **110** | **95/110** | **→ 86.4 / 100** |

**Verdict:** ⚠️ **CONDITIONALLY READY** (86.4/100)

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | Metadata: "UC227-231", Mã: "DDI_AIII2_[ID]" | Theo appendices.md, phân hệ DDI có UC227-232 (Quý, DDI_AI3) và UC233-238 (Năm, DDI_AI2). File hiện tại dùng UC227-231 với DDI_AIII2. BA xác nhận dải UC chính xác và mã biểu đúng cho báo cáo này? | Ảnh hưởng trực tiếp đến mã sinh báo cáo, truy vết UC, và mapping với Phụ lục XIV. Nếu sai sẽ gây conflict với các UC khác. | Open |
| Q2 | Medium | UC227-231.2 Phần B — Block NĐT | Đối với phân hệ ĐTTN (đầu tư trong nước), liệu cấu trúc Block NĐT có giống hệt ĐTNN (chia NĐT VN / NĐT NN) không? Hay ĐTTN chỉ có NĐT trong nước? | Nếu ĐTTN không có NĐT nước ngoài, mục 1.2 "Nhà đầu tư nước ngoài" sẽ không áp dụng — cần xác nhận để tránh hiển thị block thừa. | Open |
| Q3 | Medium | UC227-231.2 Phần B — RULE-01 | RULE-01 ghi "Đối với dự án NĐT trong nước cấp GCNĐKĐT bằng VNĐ, đổi USD sang Triệu VNĐ". Vì đây là phân hệ ĐTTN, phải chăng MẶC ĐỊNH tất cả dự án đều dùng VNĐ? Hay vẫn có trường hợp dự án ĐTTN dùng USD? | Quyết định đơn vị mặc định hiển thị trên eForm Grid. Nếu 100% ĐTTN dùng VNĐ thì RULE-01 luôn trigger và label mặc định nên là "Triệu VNĐ". | Open |
| Q4 | Medium | Metadata: "Hình thức nộp" | UC047-052 (FDI) có ghi "Hình thức nộp: Báo cáo đơn lẻ theo từng dự án". UC227-231 cũng copy y hệt. BA xác nhận ĐTTN cũng là báo cáo đơn lẻ (1 BC / 1 dự án / 1 kỳ)? | Ảnh hưởng đến logic kiểm tra trùng lặp bản ghi và hiển thị danh sách. | Open |
| Q5 | Low | UC227-231.1 — Empty state | Khi kỳ hạn "Chưa tới hạn", empty state text là "Kỳ báo cáo này chưa tới hạn. Vui lòng đợi đến thời hạn để lập báo cáo". Có cần thay đổi gì cho ĐTTN so với ĐTNN không? | Đảm bảo UX nhất quán hoặc có customization theo phân hệ. | Open |
| Q6 | Low | N/A (Missing) | Không có wireframe/mockup đi kèm cho UC227-231. BA có kế hoạch cung cấp design riêng cho ĐTTN hay dùng chung design với UC047-052 (FDI)? | Cần wireframe để cross-verify UI inventory và phát hiện gap giữa spec và design. | Open |

---

## 🟢 What's Good

- Cấu trúc tài liệu hoàn chỉnh theo template chuẩn (3 child UC: .1/.2/.3)
- Tham chiếu CMR/CF đầy đủ và chính xác cho từng trường
- eForm Grid mô tả chi tiết với cấu trúc phân cấp rõ ràng (Auto-calc, Editable, Locked)
- Business rules (RULE-01, RULE-02, RULE-03) được định nghĩa cụ thể với message lỗi
- Block NĐT có mô tả cấu trúc 6 row/block rõ ràng
- Phân quyền CMR_01 được áp dụng nhất quán

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Luồng Lập báo cáo (happy path): chọn dự án → auto-fill → nhập eForm → Lưu nháp / Nộp
- Validation số (CMR_05): ký tự hợp lệ, số âm/dương
- Auto-calc eForm Grid: công thức tính tổng
- RULE-02: đổi dự án → popup cảnh báo
- RULE-03: validate năm báo cáo
- Tác vụ bổ trợ: điều kiện hiển thị theo trạng thái
- Filter/Search trên danh sách

**What CANNOT be tested yet (blocked by gaps):**
- Q1: Nếu mã UC/mã biểu sai → toàn bộ test data và mã sinh sẽ sai
- Q2: Block NĐT cho ĐTTN — chưa rõ có NĐT nước ngoài hay không
- Q3: Đơn vị mặc định — chưa rõ ĐTTN luôn VNĐ hay có case USD

**Suggested test focus areas:**
- Happy path: Lập BC → chọn dự án → nhập eForm → Nộp thành công
- Alternative: API lỗi → nhập tay; đổi dự án → xóa Phần B
- Boundary: Số âm ở mục 2/3; số >= 0 ở các mục khác; max length 18 ký tự
- Error: Trường bắt buộc bỏ trống; sai format số; năm BC < năm cấp GCNĐKĐT
- UI: eForm Grid viền đỏ + tooltip lỗi; Auto-calc real-time; RULE-01 đổi label

---

## 📌 Summary & Recommendation

Tài liệu UC227-231 có cấu trúc hoàn chỉnh và chi tiết, được tạo từ template UC047-052 (FDI) với các tham chiếu CMR/CF đầy đủ. Tuy nhiên, có **xung đột quan trọng** giữa mã UC/mã biểu trong file và file appendices.md (Q1), cùng với câu hỏi nghiệp vụ về sự khác biệt giữa ĐTTN và ĐTNN trong cấu trúc Block NĐT (Q2) và đơn vị tiền tệ mặc định (Q3). **Khuyến nghị:** BA cần trả lời Q1-Q4 trước khi QA bắt đầu thiết kế test case. QA có thể bắt đầu chuẩn bị test scenarios cho các luồng chung (filter, search, tác vụ bổ trợ) trong khi chờ BA phản hồi.
