# UC Readiness Review — UC095-100 (Điều chỉnh GCNĐKĐT - Mẫu A.IV.6)
**Functional / Black-box Test Readiness Template v3 — Re-audit v3**

---

## Feature Brief

Chức năng cho phép các Bộ (Bộ Tư pháp / Bộ Công thương / NHNN VN) lập báo cáo định kỳ quý về tình hình điều chỉnh GCNĐKĐT theo Mẫu A.IV.6. Kiến trúc tương tự UC089-094 với phân quyền cách ly hoàn toàn giữa các Bộ. Hỗ trợ Import CF_02 Case 2 (không có Phạm vi). SRS ver 1.1 đã giải quyết 3 câu hỏi audit v2.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **86.4 / 100** | ⚠️ **CONDITIONALLY READY** |

Raw: 95/110 → Final: round((95/110)×100, 1) = **86.4/100**.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC095-100 | Điều chỉnh GCNĐKĐT - Mẫu A.IV.6 | v1.1 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-04-23 | 2026-05-07 |

---

## 1. Objective & Scope

### 1.1 Objective
Hỗ trợ các Bộ/Ngành báo cáo định kỳ quý các dự án ĐTNN có điều chỉnh GCNĐKĐT thuộc lĩnh vực quản lý của mình. Giảm nhập liệu thủ công qua tích hợp API.

### 1.2 In Scope
- Xem danh sách báo cáo theo quý.
- Lập báo cáo điều chỉnh với dynamic rows.
- Auto-fill từ API.
- Import CF_02 Case 2.
- Tác vụ bổ trợ: Xem chi tiết, Vòng đời, In, Export, Nộp, Sửa, Xóa.

### 1.3 Out of Scope
- Master data dự án.
- Phê duyệt báo cáo.
- Nộp trễ hạn.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Bộ Tư pháp | Primary | Lập, sửa, nộp báo cáo lĩnh vực Tư pháp |
| Bộ Công thương | Primary | Lập, sửa, nộp báo cáo lĩnh vực Công thương |
| NHNN VN | Primary | Lập, sửa, nộp báo cáo lĩnh vực Ngân hàng |
| Cục ĐTNN | Secondary | Nhận báo cáo, Notification |
| API GCNĐKĐT | System | Cung cấp dữ liệu auto-fill |

Phân quyền cách ly: Bộ A không thấy báo cáo của Bộ B (CMR_02).

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- User có quyền lập/xem báo cáo thuộc Bộ/Ngành.
- Kỳ báo cáo "Trong thời hạn".

### 3.2 Postconditions
| After | State |
|---|---|
| Lưu nháp | Trạng thái "Lưu nháp" |
| Nộp | "Chờ duyệt", Notification đến Cục ĐTNN, Audit log |
| Xóa | Chỉ Lưu nháp chưa từng nộp; Audit log |

---

## 4. UI Object Inventory & Mapping

SRS ver 1.1 mô tả đầy đủ bảng inventory Section UC095-100.1 (list) và UC095-100.2 (form) với:
- **Filter:** Năm, Quý, Lĩnh vực, Trạng thái kỳ hạn, Trạng thái báo cáo, Mã báo cáo
- **Bảng dữ liệu:** STT, Tên dự án, MST, các cột thông tin điều chỉnh
- **Buttons:** Lập báo cáo, Import, Lưu nháp, Nộp, Hủy, Thêm dòng, Xóa dòng
- **Footer:** Nơi lập, Ngày tháng năm

**Gap:** SRS text-only, không mockup → UI Inventory cap 10/15.

---

## 5. Object Attributes & Behavior Definition

Hành vi Mode A/B, dòng API Disabled, dynamic rows max 500, optimistic locking, cross-validate đã mô tả trong SRS. Một số element chưa có hover/focus state → cap 17/20.

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Lập Báo Cáo
**A. Workflows:** Mode A/B auto-detect, API auto-fill với dòng Disabled, cross-validate, Import CF_02 Case 2, Nộp → Chờ duyệt.

**B. Business Rules:**
| Field | Required | Format | Error |
|---|---|---|---|
| Năm | Yes | 4-digit integer | CMR_05 |
| Quý | Yes | 1–4 | — |
| Lĩnh vực | Yes | Dropdown | — |
| MST | Yes | 10–13 chars | "MST không hợp lệ" |
| Vốn điều chỉnh | Yes | Decimal USD 2dp | "Vốn phải ≥ 0" |

**C. UI/UX:** Toast T05 (API fail), P04 popup xóa dòng, Optimistic locking conflict notice.

---

## 7. Functional Integration Analysis

| Trigger | Impact | Consistency |
|---|---|---|
| Nộp | Notification Cục ĐTNN, kỳ hạn cập nhật | List refresh |
| Xóa | Chỉ Lưu nháp chưa nộp | Audit log |
| Import | CF_02 Case 2, .xlsx | Bảng dữ liệu |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|---|---|---|---|---|
| AC-01 | Mode A | API fail | Mở form | Toast T05 + Enabled toàn bộ |
| AC-02 | Mode B | API OK | Mở form | Auto-fill, dòng API Disabled |
| AC-03 | Max rows | 500 dòng | Thêm dòng | Toast "Max 500" |
| AC-04 | Empty table | 0 dòng | Nộp | Toast T07, block |
| AC-05 | Import | .xlsx < 10MB | Upload | Data đổ vào bảng |
| AC-06 | Import fail | Format sai | Upload | Toast lỗi |
| AC-07 | Role isolation | Bộ A login | Xem list | Chỉ thấy báo cáo Bộ A |
| AC-08 | Nộp | Valid | Click Nộp | "Chờ duyệt" + Notification |
| AC-09 | Concurrent edit | 2 user | User B save sau | Conflict, refresh |
| AC-10 | Xóa dòng manual | Dòng manual | Click Xóa | Popup P04, re-index STT |

---

## 9. Non-functional Requirements

| Category | Requirement |
|---|---|
| Performance | API fill + render ≤ 5s |
| Security | Role isolation CMR_02, Audit log |
| Concurrency | Optimistic locking |
| Browser Compatibility | (Missing) |
| Accessibility | (Missing WCAG) |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
(Tất cả resolved trong v2 + backlog v1)

### 10.2 Dependencies
- UC089-094 (reference Import flow).
- API GCNĐKĐT.
- CMR_02, CMR_03, CMR_04, CMR_05, CMR_07, CMR_09, CF_01–CF_09.

---

## 11. Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v3 | 2026-05-07 | QC Re-audit | Re-audit sau SRS ver 1.1. Điểm 86.4/100. |

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & Roles | 10 | 9/10 | ⚡ |
| 4 | Pre/Post-conditions | 10 | 9/10 | ⚡ |
| 5 | UI Object Inventory | 15 | 10/15 | ⚡ |
| 6 | Object Attributes | 20 | 17/20 | ⚡ |
| 7 | Functional Logic | 20 | 18/20 | ⚡ |
| 8 | Integration | 10 | 9/10 | ⚡ |
| 9 | AC | 10 | 9/10 | ⚡ |
| 10 | NFR | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **95/110** | **86.4/100** |

### Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | UI section | Thiếu mockup | Không verify visual | Open |
| G2 | Low | NFR | Thiếu Browser Compatibility, WCAG | Compatibility test blocked | Open |
| G3 | Low | Functional Logic | Import reference "tham khảo UC089-094" | Testing cần chi tiết tại UC | Open |

### 🟢 What's Good

- Phân quyền cách ly rõ ràng (CMR_02).
- Mode A/B auto-detect + optimistic locking.
- Tham chiếu CF_02 Case 2 cho Import.
- Dynamic rows + dòng API Disabled.
- AC bao phủ happy + alternative + exception.

### 🧪 Testability Outlook

**Can test now:** Role isolation, Mode A/B, dynamic rows, Import, concurrent edit, AC1–AC10.
**Cannot test yet:** UI visual (mockup), browser compat, WCAG.

### 📌 Summary & Recommendation

UC095-100 đạt 86.4/100, CONDITIONALLY READY. Tương tự UC089-094 về kiến trúc và gap. Đủ điều kiện test design với 3 gap minor song song.

---
*Re-audit v3 — 2026-05-07*
