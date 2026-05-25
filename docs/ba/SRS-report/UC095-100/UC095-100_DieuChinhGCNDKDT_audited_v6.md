# UC Readiness Review — UC095-100 (Điều chỉnh GCNĐKĐT - Mẫu A.IV.6)
**Functional / Black-box Test Readiness Template v4 — Re-audit with SRS v1.5**

| Thông tin | Giá trị |
|---|---|
| Document Title | UC095-100 Audit Report v6 |
| Date Created | 2026-05-22 |
| Author | QC Agent (SRS v1.5 Alignment) |
| Version | v6 |
| SRS Version Reviewed | 1.5 |

---

## Feature Brief

Chức năng cho phép các Bộ (Bộ Tư pháp / Bộ Công thương / NHNN VN) lập báo cáo định kỳ quý về tình hình điều chỉnh GCNĐKĐT theo Mẫu A.IV.6. SRS ver 1.5 cập nhật: Filter dropdown mặc định "Tất cả" (CMR_16), bỏ dấu `.` cuối error messages, bổ sung required error C7/C8, button state B3/B4 "Luôn Enabled", xóa dòng áp dụng tất cả dòng (không phân biệt API/user).

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **93.6 / 100** | ✅ **READY** |

Raw: 103/110 → Final: round((103/110)×100, 1) = **93.6/100**.

**Lý do tăng điểm so với v5 (92.7 → 93.6):**
- SRS v1.5 làm rõ thêm: filter default, button state, required messages, xóa dòng behavior.
- Giải quyết ambiguity về B2 (xóa dòng) — nay áp dụng tất cả dòng.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC095-100 | Điều chỉnh GCNĐKĐT - Mẫu A.IV.6 | v1.5 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-04-23 | 2026-05-22 |

---

## 1. Objective & Scope

### 1.1 Objective
Hỗ trợ các Bộ/Ngành báo cáo định kỳ quý các dự án ĐTNN có điều chỉnh GCNĐKĐT thuộc lĩnh vực quản lý của mình. Giảm nhập liệu thủ công qua auto-load từ DB + cho phép user hiệu chỉnh toàn bộ.

### 1.2 In Scope
- Xem danh sách báo cáo theo quý (UC095-100.1).
- Lập báo cáo điều chỉnh với Dynamic Table — 2 nguồn dữ liệu (UC095-100.2).
- Auto-load dữ liệu từ DB, auto-fill khi nhập C2.
- Import CF_02 Case 2 (không có Phạm vi).
- Tác vụ bổ trợ: Xem chi tiết, Vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa, Xóa (UC095-100.3).

### 1.3 Out of Scope
- Master data dự án (phân hệ khác).
- Phê duyệt báo cáo (phía Bộ Tài chính).
- Quy trình xử lý sau khi báo cáo được tiếp nhận.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Bộ Tư pháp | Primary | Lập, sửa, nộp báo cáo lĩnh vực "CÔNG TY LUẬT" |
| Bộ Công thương | Primary | Lập, sửa, nộp báo cáo lĩnh vực "DẦU KHÍ" |
| NHNN VN | Primary | Lập, sửa, nộp báo cáo lĩnh vực "NGÂN HÀNG NƯỚC NGOÀI" |
| Cục ĐTNN (Bộ Tài chính) | Secondary | Nhận báo cáo |
| Hệ thống DB | System | Cung cấp dữ liệu auto-load/auto-fill |

Phân quyền cách ly hoàn toàn: Bộ A không thấy/thao tác báo cáo của Bộ B (CMR_02).

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- User có quyền lập/xem báo cáo thuộc Bộ/Ngành.
- Kỳ báo cáo "Trong thời hạn" (để Lập/Nhập từ file).

### 3.2 Postconditions
| After | State |
|---|---|
| Lưu nháp | Trạng thái "Lưu nháp", sort persist |
| Nộp | "Chờ duyệt", Audit log |
| Xóa | Chỉ Lưu nháp chưa từng nộp; Audit log |

---

## 4. UI Object Inventory & Mapping

### 4.1 Wireframe vs SRS Cross-check

#### Màn hình Danh sách (Danh sách.png)

| # | Element (Wireframe) | SRS Field | Match |
|---|---|---|---|
| 1 | Yearpicker "Năm" | Row #1 — Yearpicker | ✅ Khớp |
| 2 | Dropdown "Trạng thái kỳ" | Row #2 — Multiple-selection Dropdown, default "Tất cả" | ✅ Khớp |
| 3 | Dropdown "Trạng thái báo cáo" | Row #3 — Multiple-selection Dropdown, default "Tất cả" | ✅ Khớp |
| 4 | Search bar "Mã báo cáo" | Row #4 — Search bar | ✅ Khớp |
| 5 | Kỳ hạn collapse/expand | Row #5 — Label, collapse | ✅ Khớp |
| 6 | Badge trạng thái kỳ | Row #6 — Label | ✅ Khớp |
| 7 | Nút "Lập báo cáo" | Row #7 — Button | ✅ Khớp |
| 8 | Nút "Nhập từ file" | Row #8 — Button | ✅ Khớp |
| 9 | Cột: Mã BC, Lĩnh vực, Ngày cập nhật, Trạng thái, Hành động | Row #9-13 | ✅ Khớp |

**Kết luận:** Wireframe Danh sách khớp 100% với SRS v1.5.

#### Màn hình Lập báo cáo (Lập báo cáo.png)

| # | Element (Wireframe) | SRS Field | Match |
|---|---|---|---|
| 1 | Tên Bộ/Ngành (disabled) | Header #1 — Label, Auto-fill | ✅ Khớp |
| 2 | Lĩnh vực báo cáo (text input) | Header #2 — Text input | ✅ Khớp |
| 3 | Quý báo cáo (disabled) | Header #3 — Dropdown, Disabled | ✅ Khớp |
| 4 | Năm báo cáo (disabled) | Header #4 — Yearpicker, Disabled | ✅ Khớp |
| 5 | Bảng: STT, C2-C9 | Dynamic Table C1-C9 | ✅ Khớp |
| 6 | Nút Thêm dòng | B1 — Button | ✅ Khớp |
| 7 | Icon Xóa dòng (tất cả dòng) | B2 — Icon Button (mỗi dòng) | ✅ Khớp |
| 8 | Nút Lưu nháp | B3 — Button (Luôn Enabled) | ✅ Khớp |
| 9 | Nút Nộp báo cáo | B4 — Button (Luôn Enabled) | ✅ Khớp |
| 10 | Nút Hủy | B1(Hủy) — Button | ✅ Khớp |

**Kết luận:** Wireframe Lập báo cáo khớp 100% với SRS v1.5.

#### Màn hình Xem chi tiết (Xem chi tiết.png)

| # | Element (Wireframe) | SRS Field | Match |
|---|---|---|---|
| 1 | Layout giống form Lập, tất cả Disabled | CF_07 — toàn bộ trường Disabled | ✅ Khớp |
| 2 | Nút In | UC095-100.3 #5 — Button | ✅ Khớp |
| 3 | Nút Xuất báo cáo | UC095-100.3 #6 — Button | ✅ Khớp |

**Kết luận:** Wireframe Xem chi tiết khớp với SRS.

**Score: 14/15** — Wireframe khớp 100% SRS. Trừ 1 điểm: Wireframe không thể hiện chi tiết placeholder text, counter ký tự (cần dev verify).

---

## 5. Object Attributes & Behavior Definition

### 5.1 Dynamic Table Behavior (SRS ver 1.5)

| Aspect | Dòng auto-load | Dòng user thêm tay |
|---|---|---|
| Khởi tạo | Hệ thống query DB, load sẵn C2→C9 | User nhấn [Thêm dòng], dòng trống |
| C2 | Auto-fill, Editable | User nhập thủ công, check tồn tại khi blur |
| C3-C4 | Auto-fill, Editable | Auto-fill sau khi C2 hợp lệ, Editable |
| C5 | Auto-fill, Read-only | Auto-fill sau khi C2 hợp lệ, Read-only |
| C6 | Auto-fill, Editable | Enabled, user nhập |
| C7-C9 | Auto-fill, Editable | Enabled, user nhập |
| Xóa | ✅ Cho phép (popup xác nhận) | ✅ Cho phép (popup xác nhận) |

> **Thay đổi v1.5:** B2 (Xóa dòng) hiển thị trên **tất cả dòng** — không phân biệt dòng API hay dòng user. Popup xác nhận: "Bạn có chắc chắn muốn xóa dòng này?" với nút [Đồng ý] / [Hủy].

### 5.2 Validation Rules (Updated SRS v1.5)

| Rule | Trigger | Error Message |
|---|---|---|
| C2 không tồn tại trong DB | Blur khỏi C2 | "Mã dự án này chưa được khởi tạo trên hệ thống. Vui lòng kiểm tra lại" |
| C6 < C3 | Blur/Submit | "Ngày điều chỉnh không được nhỏ hơn ngày cấp dự án" |
| C6 > today | Blur/Submit | "Không được chọn ngày ở tương lai" |
| C7 == C8 (sau trim) | Blur C8 / Submit | "Nội dung trước và sau điều chỉnh không được giống nhau" |
| Bảng 0 dòng + Nộp | Submit | Chặn nộp + Toast |
| C2 max 50 ký tự | Input | CMR_06. Error: "Mã số dự án nhập quá ký tự cho phép" |
| C7/C8 max 1000 ký tự | Input | CMR_06. Bộ đếm ký tự. Error: "[Tên trường] nhập quá ký tự cho phép" |
| C9 max 500 ký tự | Input | CMR_06. Bộ đếm ký tự. Error: "Ghi chú nhập quá ký tự cho phép" |
| C7 bắt buộc | Submit | "Vui lòng nhập Nội dung điều chỉnh trước" |
| C8 bắt buộc | Submit | "Vui lòng nhập Nội dung điều chỉnh sau" |

> **Thay đổi v1.5 so với v5 audit:**
> - C2 max: **50 ký tự** (SRS v1.5 ghi rõ "Tối đa 50 ký tự") — v5 audit ghi 255 là SAI, đã sửa.
> - C7/C8 max: **1000 ký tự** (SRS v1.5 ghi "tối đa 1000") — v5 audit ghi 3000 là SAI, đã sửa.
> - C9 max: **500 ký tự** (SRS v1.5 ghi "500 ký tự") — v5 audit ghi 255 là SAI, đã sửa.
> - Error messages: Bỏ dấu `.` cuối 3 messages (C2 check, C6<C3, C6>today).
> - Error max length format: Theo CMR_06 v2.0 — "[Tên trường] nhập quá ký tự cho phép".

### 5.3 Sort Behavior
- Cột C3 (Ngày cấp) và C6 (Ngày điều chỉnh): có icon sort trên header.
- Mặc định: C6 descending (xa nhất → gần nhất).
- Toggle: Ascending ↑ / Descending ↓.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.

### 5.4 Filter Behavior (Updated v1.5)
- Dropdown "Trạng thái kỳ" và "Trạng thái báo cáo": Mặc định chọn **"Tất cả"** (CMR_16).
- Kết quả lọc hiển thị ngay (real-time), không cần nhấn nút.

### 5.5 Button States (Updated v1.5)
| Button | State | Ghi chú |
|---|---|---|
| B3 — Lưu nháp | **Luôn Enabled** | Không phụ thuộc validate |
| B4 — Nộp báo cáo | **Luôn Enabled** | Validate khi nhấn |

### 5.6 Wireframe Confirmation
- ✅ Wireframe "Lập báo cáo" xác nhận layout bảng với đầy đủ cột C1-C9.
- ✅ Icon sort hiển thị trên header (khớp SRS).
- ✅ Nút Thêm dòng + Icon Xóa dòng hiển thị đúng vị trí.
- ✅ Icon Xóa dòng hiển thị trên tất cả dòng (khớp SRS v1.5).

**Score: 20/20** — Đầy đủ behavior definition. SRS v1.5 giải quyết ambiguity về xóa dòng và button state.

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Workflow: Lập Báo Cáo

```
[Danh sách] → Click [Lập báo cáo] (kỳ Trong thời hạn)
    → Mở form → Auto-load dòng từ DB (C2→C9 filled)
    → User có thể:
        a) Hiệu chỉnh dòng auto-load (tất cả Editable)
        b) Thêm dòng mới → Nhập C2 → Blur → Check DB
            → Hợp lệ: Auto-fill C3→C9
            → Không hợp lệ: Cảnh báo inline
        c) Xóa bất kỳ dòng nào (popup xác nhận)
    → [Lưu nháp] hoặc [Nộp báo cáo]
        → Nộp: Validate all → Success: "Chờ duyệt"
```

### 6.2 Workflow: Xem & Tác vụ bổ trợ

```
[Danh sách] → Cột Hành động:
    → [Xem chi tiết]: Toàn bộ Disabled (CF_07)
    → [Chỉnh sửa]: Chỉ khi Lưu nháp / Yêu cầu chỉnh sửa
    → [Nộp]: Chỉ khi Lưu nháp (CF_09)
    → [Xem vòng đời]: Popup Audit Trail (CF_06)
    → [In]: CF_05
    → [Xuất báo cáo]: Excel (CF_04)
    → [Xóa]: Chỉ Lưu nháp + chưa từng nộp (CF_08)
```

### 6.3 Business Rules (Updated from SRS v1.5)

| Rule | Description |
|---|---|
| Phân quyền cách ly | Mỗi Bộ chỉ thấy/thao tác BC của mình (CMR_02) |
| Kỳ hạn control | Lập/Nhập chỉ khi "Trong thời hạn" |
| Auto-suggest Lĩnh vực | Bộ CT → "DẦU KHÍ"; Bộ TP → "CÔNG TY LUẬT"; NHNN → "NGÂN HÀNG NƯỚC NGOÀI" |
| C2 reset | Xóa/sửa C2 sau auto-fill → Clear C3→C9 |
| C5 unique per report | Cùng mã GCNĐT nhiều dòng → n tăng dần, không trùng |
| Concurrent edit | Last Write Wins + Lifecycle Log (CF_06) |
| Mã báo cáo | FDI_AIV6_[ID] — auto-increment, global unique |
| Filter default | Trạng thái kỳ + Trạng thái BC mặc định "Tất cả" (CMR_16) |
| Xóa dòng | Tất cả dòng đều cho phép xóa (không phân biệt API/user) |

**Score: 19/20** — Logic rõ ràng, workflow đầy đủ. Trừ 1 điểm: Chưa mô tả chi tiết behavior khi API/DB timeout trong quá trình auto-load.

---

## 7. Functional Integration Analysis

| Trigger | Source | Target | Behavior |
|---|---|---|---|
| Lập báo cáo | UC095-100.1 | UC095-100.2 | Truyền Quý + Năm, mở form |
| Auto-load | DB | Form | Query dữ liệu điều chỉnh theo quý |
| Check C2 | Form (blur) | DB | Tra cứu mã dự án |
| Nộp | Form | System | Trạng thái → "Chờ duyệt", Audit log |
| Import | CF_02 Case 2 | Form | Load data từ file (ref UC089-094) |
| Xuất báo cáo | Form/Detail | Excel | CF_04 |
| Xem vòng đời | List | Popup | CF_06 Audit Trail |

**Score: 9/10** — Tích hợp rõ ràng. Trừ 1: Import flow vẫn reference UC089-094 (acceptable).

---

## 8. Acceptance Criteria (from SRS v1.5)

| AC # | Mô tả | Testable |
|---|---|---|
| AC1 | Auto-load: Mở form → hệ thống load dòng từ DB, tất cả Editable | ✅ |
| AC2 | C2 không tồn tại → cảnh báo inline, không auto-fill | ✅ |
| AC3 | C2 hợp lệ → auto-fill C3→C9, tất cả Editable | ✅ |
| AC4 | C6 < C3 hoặc C6 > today → lỗi inline | ✅ |
| AC5 | C7 == C8 (sau trim) → lỗi inline tại C8 | ✅ |
| AC6 | Sort mặc định C6 descending, toggle, persist khi Lưu nháp | ✅ |
| AC7 | Xóa dòng → popup xác nhận → re-index STT | ✅ |
| AC8 | Bảng 0 dòng + Nộp → chặn + Toast | ✅ |
| AC9 | Concurrent edit: Last Write Wins + Lifecycle Log | ✅ |

**Score: 10/10** — AC đầy đủ, testable, bao phủ happy + alternative + exception paths.

---

## 9. Non-functional Requirements

| Category | Requirement | Source |
|---|---|---|
| Performance | Thời gian tải danh sách < 3s. API timeout: 5s | SRS v1.5 NFR |
| Security | RBAC + Cách ly hoàn toàn giữa các Bộ. Audit log | CMR_02 |
| Concurrency | Last Write Wins + Lifecycle Log | CF_06 |
| Tab Navigation | Tab/Shift+Tab chuyển focus theo thứ tự form | CMR_18 |
| Browser Compatibility | (Không đề cập trong SRS) | — |
| Accessibility | (Không đề cập WCAG trong SRS) | — |

**Score: 4/5** — Có Performance + Security + Concurrency + Tab Navigation. Thiếu Browser Compatibility và WCAG (minor).

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

| ID | Priority | Question | Status |
|---|---|---|---|
| Q1 | Low | Browser Compatibility: SRS không nêu danh sách browser hỗ trợ | Open |
| Q2 | Low | WCAG: Không có yêu cầu accessibility cụ thể | Open |

### 10.2 Resolved Questions (from v5)

| ID | Question | Resolution |
|---|---|---|
| G1 (v3) | Thiếu mockup/wireframe | ✅ RESOLVED — Đã có 3 wireframe đầy đủ |
| G3 (v3) | Import reference UC089-094 | ✅ Acceptable — Cross-reference pattern |
| G4 (v5) | Hover/focus state chưa mô tả | ✅ RESOLVED — CMR_18 bổ sung Tab Navigation |

### 10.3 Dependencies
- UC089-094 (reference Import flow CF_02 Case 2).
- CMR_02, CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_08, CMR_09, CMR_10, CMR_12, CMR_14, CMR_16, CMR_18.
- CF_01 → CF_09.

---

## 11. Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-04-23 | QC Audit | Initial audit |
| v2 | 2026-05-03 | QC Re-audit | Re-audit sau BA trả lời |
| v3 | 2026-05-07 | QC Re-audit | Re-audit sau SRS ver 1.1. Điểm 86.4/100 |
| v4 | 2026-05-21 | QC Re-audit | Re-audit với wireframe + SRS ver 1.4. Điểm 92.7/100 |
| v5 | 2026-05-22 | QC Re-audit | CMR Alignment. Điểm 92.7/100 |
| v6 | 2026-05-22 | QC Re-audit | Re-audit SRS v1.5. Sửa max length C2/C7/C8/C9. Điểm 93.6/100 |

---

## Audit Summary

| # | Knowledge Area | Max | Score v5 | Score v6 | Delta | Notes |
|---|---|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | 5/5 | — | Đầy đủ |
| 2 | Objective & Scope | 5 | 5/5 | 5/5 | — | Đầy đủ |
| 3 | Actors & Roles | 10 | 10/10 | 10/10 | — | Đầy đủ |
| 4 | Pre/Post-conditions | 10 | 9/10 | 9/10 | — | Đầy đủ |
| 5 | UI Object Inventory | 15 | 14/15 | 14/15 | — | Wireframe khớp SRS |
| 6 | Object Attributes | 20 | 19/20 | 20/20 | +1 | SRS v1.5 giải quyết ambiguity xóa dòng + button state |
| 7 | Functional Logic | 20 | 19/20 | 19/20 | — | Workflow rõ ràng |
| 8 | Integration | 10 | 9/10 | 9/10 | — | Import vẫn ref UC089-094 |
| 9 | AC | 10 | 10/10 | 10/10 | — | AC1-AC9 đầy đủ |
| 10 | NFR | 5 | 4/5 | 4/5 | — | Vẫn thiếu browser/WCAG |
| **Total** | | **110** | **102/110** | **103/110** | **+1** | **92.7 → 93.6** |

---

### Unified Gap & Question Report

| ID | Priority | Ref | Issue | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | ~~Medium~~ | ~~UI section~~ | ~~Thiếu mockup~~ | ~~Không verify visual~~ | ✅ **RESOLVED** (wireframe provided) |
| G2 | Low | NFR | Thiếu Browser Compatibility, WCAG | Compatibility test blocked | Open (minor) |
| G3 | ~~Low~~ | ~~Functional Logic~~ | ~~Import ref UC089-094~~ | ~~Testing cần chi tiết~~ | ✅ **RESOLVED** (acceptable cross-ref) |
| G4 | ~~Low~~ | ~~Object Attributes~~ | ~~Hover/focus state~~ | ~~UI polish~~ | ✅ **RESOLVED** (CMR_18 Tab Navigation) |
| G5 | Low | Functional Logic | Chưa mô tả behavior khi DB timeout trong auto-load | Error handling edge case | Open (minor) |

---

### 🟢 What's Good

- **Wireframe khớp 100% SRS** — Cả 3 màn hình (Danh sách, Lập báo cáo, Xem chi tiết) đều match hoàn toàn với mô tả SRS v1.5.
- Phân quyền cách ly rõ ràng (CMR_02).
- Dynamic Table 2 nguồn dữ liệu được mô tả chi tiết (auto-load + user thêm tay).
- **Xóa dòng áp dụng tất cả dòng** — SRS v1.5 giải quyết ambiguity từ v1.2.
- Validation rules đầy đủ với error message cụ thể (không dấu `.` cuối).
- Sort behavior + persist rõ ràng.
- AC1-AC9 bao phủ happy + alternative + exception paths.
- Filter dropdown mặc định "Tất cả" (CMR_16).
- Button state B3/B4 "Luôn Enabled" được ghi rõ.
- Required error C7/C8 có message cụ thể.
- Concurrent edit strategy rõ (Last Write Wins + Lifecycle Log).

### 🔴 Remaining Gaps (All Minor)

1. **G2:** Thiếu Browser Compatibility + WCAG — common gap, không block test design.
2. **G5:** DB timeout behavior khi auto-load — edge case, có thể infer từ NFR (API timeout 5s) + CMR_12 (API thất bại → Toast lỗi + Enabled).

### 🧪 Testability Outlook

**Can test now (đủ thông tin):**
- Role isolation (CMR_02)
- Dynamic Table: auto-load, thêm dòng, xóa bất kỳ dòng nào
- Validation: C2 check, C6 vs C3, C7 vs C8, empty table, max length (C2=50, C7/C8=1000, C9=500)
- Required: C7, C8 required messages
- Sort: default, toggle, persist
- Filter: Năm, Trạng thái kỳ (default "Tất cả"), Trạng thái BC (default "Tất cả"), Mã BC
- Tác vụ bổ trợ: Xem chi tiết, Nộp, Chỉnh sửa, Xóa, In, Xuất
- Import CF_02 Case 2
- Concurrent edit (Last Write Wins)
- UI layout verification (wireframe available)
- Button state: B3/B4 Luôn Enabled
- Tab Navigation (CMR_18)

**Cannot test yet (minor gaps):**
- Browser compatibility matrix
- WCAG compliance

### 📌 Summary & Recommendation

UC095-100 đạt **93.6/100**, verdict **READY**. SRS v1.5 giải quyết thêm ambiguity về xóa dòng, button state, filter default. Tất cả gap còn lại đều ở mức Low priority và không block test design. **Đề xuất: Tiến hành test scenario design ngay.**

---

### Wireframe Evidence Summary

| Wireframe | File | Đối chiếu | Kết quả |
|---|---|---|---|
| Danh sách | Danh sách.png | 9/9 elements khớp SRS | ✅ 100% match |
| Lập báo cáo | Lập báo cáo.png | 10/10 elements khớp SRS | ✅ 100% match |
| Xem chi tiết | Xem chi tiết.png | 3/3 elements khớp SRS | ✅ 100% match |

---

## Changelog v6 (SRS v1.5 Alignment — 2026-05-22)

| # | Hạng mục | Thay đổi |
|---|---|---|
| 1 | C2 maxlength | 255 (v5 sai) → **50 ký tự** (SRS v1.5 ghi rõ) |
| 2 | C7/C8 maxlength | 3000 (v5 sai) → **1000 ký tự** (SRS v1.5 ghi rõ) |
| 3 | C9 maxlength | 255 (v5 sai) → **500 ký tự** (SRS v1.5 ghi rõ) |
| 4 | B2 Xóa dòng | "Chỉ dòng user" (v5) → **Tất cả dòng** (SRS v1.5) |
| 5 | Filter default | Bổ sung "Tất cả" cho Trạng thái kỳ + Trạng thái BC (CMR_16) |
| 6 | Error messages | Bỏ dấu `.` cuối (C2 check, C6<C3, C6>today) |
| 7 | Required C7/C8 | Bổ sung "Vui lòng nhập Nội dung điều chỉnh trước/sau" |
| 8 | Button state B3/B4 | Bổ sung ghi chú "Luôn Enabled" |
| 9 | Error max length format | Cập nhật theo CMR_06 v2.0: "[Tên trường] nhập quá ký tự cho phép" |
| 10 | G4 resolved | CMR_18 Tab Navigation giải quyết hover/focus gap |
| 11 | Score | Object Attributes: 19→20 (+1). Total: 102→103. Final: 92.7→93.6 |

---
*Re-audit v6 — 2026-05-22 — SRS v1.5 Alignment*
