# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tai lieu:** UC101-106_TamNgungChamDutDTNN.md (phien ban 1.1)
**Ngay tao:** 2026-05-07
**Tac gia:** QC Agent (Deep Re-audit v4)
**Phien ban report:** v4

---

## Feature Brief

Chuc nang bao cao tinh hinh tam ngung, cham dut hoat dong du an DTNN theo linh vuc (Mau A.IV.7) danh cho cac Bo (Tu phap, Cong thuong, NHNN VN). Bao cao dinh ky quy, gui le (single report form), khong co pham vi du lieu nguon input. He thong ho tro auto-fill tu API cua cac Bo/Nganh de lay danh sach du an co Quyet dinh tam ngung/cham dut trong ky bao cao. Form gom 2 phan: Phan I (Tam ngung) va Phan II (Cham dut), moi phan la bang dong (dynamic rows). Cho phep them dong thu cong khi du lieu chua kip cap nhat tren API.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `83 / 110 → 75.5 / 100` | CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC101-106 | Bao cao tam ngung, cham dut hoat dong du an DTNN theo linh vuc (Mau A.IV.7) | v1.1 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | (Chua xac nhan) | 2026-04-23 | 2026-05-06 |

---

## 1. Feature Identity

| Criteria | Assessment |
|----------|-----------|
| UC-ID | UC101-106 — ro rang, duy nhat |
| Ten chuc nang | Bao cao tinh hinh tam ngung, cham dut hoat dong du an DTNN theo linh vuc (Mau A.IV.7) |
| Mau bieu | A.IV.7 |
| Phan he | Quan ly dau tu nuoc ngoai vao Viet Nam |
| BA phu trach | yen.le2 |
| Giao dien | Admin site |

**Diem:** 5/5
**Danh gia:** Clear
**Nhan xet:** Day du ID, ten, linh vuc, phan he, mau bieu. Khong co gi thieu.

---
## 2. Objective & Scope

### 2.1 Objective
Ho tro cac Bo/Nganh (Bo Tu phap, Bo Cong thuong, NHNN) bao cao dinh ky danh sach cac du an DTNN bi tam ngung hoac cham dut hoat dong thuoc linh vuc quan ly. Tich hop API de tu dong loc va lay du lieu, giam thieu nhap lieu thu cong.

### 2.2 In Scope
- Xem danh sach bao cao (nhom theo ky han quy)
- Lap bao cao moi (Create) voi 2 phan bang dong
- Chinh sua bao cao (Edit)
- Xoa bao cao (Delete)
- Nop bao cao (Submit)
- Xem chi tiet (View Detail)
- In bao cao (Print)
- Ket xuat bao cao (Export)
- Import bao cao
- Xem vong doi (Audit Trail)

### 2.3 Out of Scope
- Khong xu ly truong hop nop tre han (ky han dong se khong hien thi nut Lap/Import)
- Khong xu ly quy trinh duyet phia Cuc DTNN

**Diem:** 4/5
**Danh gia:** Partial
**Nhan xet:** Objective va Scope ro rang. Tuy nhien, thieu mo ta cu the ve Import (CF_02) - SRS chi tham chieu CF_02 nhung khong ghi ro template format la .xlsx hay .docx, cung khong ghi ro bao cao nay thuoc Case 1 hay Case 2 cua CF_02 (co Pham vi hay khong co Pham vi). Theo bang thuoc tinh "Pham vi bao cao = Khong co pham vi" -> phai la Case 2, nhung SRS khong xac nhan dieu nay.

---
## 3. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Bo Tu phap | Primary | Lap, sua, xoa, nop, xem bao cao thuoc linh vuc "HANH NGHE LUAT SU" |
| Bo Cong thuong | Primary | Lap, sua, xoa, nop, xem bao cao thuoc linh vuc "THUONG MAI/NHUONG QUYEN THUONG MAI" |
| Ngan hang Nha nuoc VN | Primary | Lap, sua, xoa, nop, xem bao cao thuoc linh vuc "NGAN HANG" |
| He thong (API) | System | Tu dong loc va dien du lieu du an tu CSDL Bo/Nganh |
| Cuc DTNN | Receiver | Nhan bao cao sau khi nop |

**Diem:** 8/10
**Danh gia:** Partial
**Nhan xet:** Phan quyen tham chieu CMR_02 nhung UC nay KHONG phai la bao cao cua NDT/TCKT (khong phai DTNN/DTTN theo CMR_01, cung khong phai DTRNN theo CMR_02). Day la bao cao cua CO QUAN BAN NGANH. SRS khong dinh nghia ro mo hinh phan quyen cho truong hop nay:
- Ai trong Bo co quyen lap? Tat ca user thuoc Bo hay chi user duoc chi dinh?
- Neu nhieu user cung Bo cung lap bao cao cho cung ky -> co chong cheo khong?
- CMR_02 noi "mot ban ghi duy nhat moi ky" nhung ap dung cho NDT, khong ro co ap dung cho Bo/Nganh khong.

---
## 4. Preconditions & Postconditions

### 4.1 Preconditions
- Nguoi dung co tai khoan thuoc to chuc tuong ung (Bo Tu phap / Cong thuong / NHNN) va co quyen lap bao cao.
- Ky bao cao dang o trang thai "Trong thoi han" (CMR_04).
- He thong API cua Bo/Nganh kha dung (hoac fallback cho phep nhap tay).

### 4.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Nop bao cao thanh cong | Bao cao chuyen trang thai "Cho duyet", he thong gui notification cho Cuc DTNN. Ghi Audit log. |
| Luu nhap thanh cong | Bao cao o trang thai "Luu nhap", hien thi trong danh sach. |
| Xoa bao cao thanh cong | Ban ghi bi xoa khoi danh sach. Ghi Audit log. |
| Chinh sua va luu | Bao cao giu nguyen trang thai hien tai (Luu nhap hoac Yeu cau chinh sua). Ghi Audit log. |

**Diem:** 8/10
**Danh gia:** Partial
**Nhan xet:** Pre/Post-conditions co nhung con thieu:
- Khong ro precondition ve so luong bao cao toi da moi ky moi Bo (1 hay nhieu?).
- Postcondition khong mo ta truong hop API timeout -> fallback state la gi (form van mo nhung tat ca truong API o trang thai Enabled?).
- Thieu postcondition cho Import thanh cong.

---
## 5. UI Object Inventory & Mapping

### 5.1 Man hinh Danh sach (Listing Screen)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|
| 1 | Filter | "Nam" | Yearpicker | No | Nam hien tai | — | — | Loc theo nam. Tu dong loc khi chon. Tham chieu: CMR_07. |
| 2 | Filter | "Trang thai ky" | Multiple-selection Dropdown | No | Null | — | Chua toi han / Trong thoi han / Qua ky bao cao | Loc theo trang thai ky han. Tham chieu: CMR_04, CMR_07. |
| 3 | Filter | "Trang thai bao cao" | Multiple-selection Dropdown | No | Null | — | Luu nhap / Cho duyet / Da tiep nhan / Yeu cau chinh sua | Tham chieu: CMR_03, CMR_07. |
| 4 | Filter | "Ma bao cao" | Search bar | No | Null | "Nhap du lieu" | — | Tim kiem theo ma bao cao. Tham chieu: CMR_06, CMR_09. |
| 5 | Ky han header | "Ky han bao cao" | Label (collapsible) | — | Collapse | — | — | VD: "Quy 1 Nam 2026". Click de expand. Tham chieu: CMR_08. |
| 6 | Ky han header | "Trang thai ky" | Label/Badge | — | — | — | Chua toi han / Trong thoi han / Qua ky bao cao | Tham chieu: CMR_04. |
| 7 | Ky han header | "Lap bao cao" | Button | — | — | — | — | Chi hien khi ky "Trong thoi han". Tham chieu: CF_01, CMR_04. |
| 8 | Ky han header | "Import" | Button | — | — | — | — | Chi hien khi ky "Trong thoi han". Tham chieu: CF_02, CMR_04. |
| 9 | Bang bao cao | "Ma bao cao" | Label (column) | — | — | — | — | Ma tu dong sinh. Tham chieu: CMR_09. Pattern: DTNN_A4_7_[ID]. |
| 10 | Bang bao cao | "Ngay nop/cap nhat" | Label (column) | — | — | — | — | Format: dd/MM/yyyy HH:mm. |
| 11 | Bang bao cao | "Trang thai bao cao" | Label/Badge (column) | — | — | — | — | Tham chieu: CMR_03. |
| 12 | Bang bao cao | "Hanh dong" | Button group (column) | — | — | — | — | Chua cac nut: Nop, Chinh sua, Xem chi tiet, Xem vong doi, In, Export, Xoa. |

### 5.2 Man hinh Lap bao cao (Create/Edit Form)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|
| 13 | Header | "Ten Bo/Nganh" | Label | — | Tu dong dien | — | — | Theo to chuc cua User Login. |
| 14 | Header | "Linh vuc bao cao" | Dropdown | Yes | Goi y theo to chuc | — | HANH NGHE LUAT SU / THUONG MAI/NHUONG QUYEN THUONG MAI / NGAN HANG | Tieu de "TRONG LINH VUC...". User co the thay doi. |
| 15 | Phan I: Tam ngung - Bang | "STT" | Integer (auto) | — | Auto increment | — | — | So thu tu tang dan. |
| 16 | Phan I: Tam ngung - Bang | "Ma so du an / So GCNDT" | Text | Yes | Auto-fill / Null | — | — | Max 50 ky tu. Disabled neu tu API. Validate: khong trung trong cung Phan I. |
| 17 | Phan I: Tam ngung - Bang | "Ngay cap" | Datepicker | Yes | Auto-fill / Null | DD/MM/YYYY | — | Ngay chung nhan lan dau. Disabled neu tu API. Validate: <= Ngay QD (cot 9). |
| 18 | Phan I: Tam ngung - Bang | "Ten du an / doanh nghiep" | Text | Yes | Auto-fill / Null | — | — | Max 250 ky tu. Disabled neu tu API. |
| 19 | Phan I: Tam ngung - Bang | "Von dau tu dang ky (USD)" | Decimal | Yes | Auto-fill / Null | — | — | So thuc duong, format 1,500,000.00. Bat buoc > 0. Disabled neu tu API. Tham chieu: CMR_05. |
| 20 | Phan I: Tam ngung - Bang | "So QD/Cong van" | Text | Yes | Auto-fill / Null | — | — | Max 50 ky tu. Disabled neu tu API. |
| 21 | Phan I: Tam ngung - Bang | "Ngay QD/Cong van" | Datepicker | Yes | Auto-fill / Null | DD/MM/YYYY | — | Disabled neu tu API. Validate: >= Ngay cap VA nam tron trong Quy/Nam ky bao cao. |
| 22 | Phan I: Tam ngung - Bang | "Ghi chu" | Textarea | No | Auto-fill / Null | — | — | Max 500 ky tu. User LUON duoc phep sua (ke ca dong API). |
| 23 | Phan II: Cham dut - Bang | (Cac cot giong Phan I: STT, Ma so du an, Ngay cap, Ten du an, Von dau tu, So QD, Ngay QD, Ghi chu) | (Giong Phan I) | (Giong Phan I) | — | — | — | Tuong tu Phan I nhung danh cho du an cham dut. Cross-section validate voi Phan I. |
| 24 | Action - Phan I | "Them dong" | Button | — | — | — | — | O cuoi Phan I, them dong trong thu cong. |
| 25 | Action - Phan II | "Them dong" | Button | — | — | — | — | O cuoi Phan II, them dong trong thu cong. |
| 26 | Action - Dong | "Xoa dong" | Button/Icon | — | — | — | — | Xoa dong tuong ung. SRS ghi "chi ap dung voi cac dong them bang tay, hoac API tuy thiet ke". |
| 27 | Footer | "Luu nhap" | Button | — | — | — | — | Tham chieu: CF_01. |
| 28 | Footer | "Nop bao cao" | Button | — | — | — | — | Tham chieu: CF_01. |
| 29 | Footer | "Xem chi tiet" (PDF Preview) | Button | — | — | — | — | Tham chieu: CF_01 (CF_07.1). |
| 30 | Footer | "Huy" | Button | — | — | — | — | Tham chieu: CF_01, CMR_14. |

**Diem:** 12/15
**Danh gia:** Partial
**Nhan xet:**
- Phan II khong duoc liet ke chi tiet tung cot rieng biet trong SRS (chi ghi "ap dung chung") -> QC phai suy luan. Nen co bang rieng cho Phan II de tranh nham lan.
- Thieu mo ta cu the cho cot "Xoa dong": dieu kien hien thi icon Xoa tren tung dong (dong API co hien thi icon Xoa khong?). SRS ghi mo ho "chi ap dung voi cac dong them bang tay, hoac API tuy thiet ke nhung thuong dong thu cong moi xoa duoc" -> KHONG xac dinh duoc.
- Thieu thong tin ve so dong toi da moi Phan (max rows).
- Thieu thong tin ve do chinh xac thap phan cua truong Von (bao nhieu chu so sau dau phay?).

---
## 6. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Truong "Linh vuc bao cao" (Dropdown) | Enabled. Default goi y theo to chuc user. | Click: Mo danh sach. Chon: Thay doi linh vuc -> API re-fetch du lieu theo linh vuc moi. | Khi thay doi linh vuc, he thong co goi lai API de cap nhat du lieu bang khong? SRS KHONG ghi ro. |
| Cac truong cot 4-9 (dong API) | Disabled sau khi API tra ve du lieu. | Khong cho phep tuong tac (read-only). | Gia tri tu dong dien tu API. Neu API tra null -> chuyen Enabled (CMR_12). |
| Cac truong cot 4-9 (dong thu cong) | Enabled. | Click: Cho phep nhap lieu. | User nhap tay toan bo. Validate khi Luu nhap/Nop. |
| Truong "Ghi chu" (cot 10) | Luon Enabled (ca dong API lan dong thu cong). | Click: Cho phep nhap/sua. | Max 500 ky tu. Auto-fill tu CSDL neu co, nhung user luon duoc sua. |
| Nut "Them dong" | Luon Enabled khi form dang o che do Create/Edit. | Click: Them 1 dong trong o cuoi Phan tuong ung. | Dong moi co tat ca truong Enabled. STT tu dong tang. |
| Nut "Xoa dong" | Hien thi tren dong thu cong (MO HO voi dong API). | Click: Xoa dong khoi bang. | Khong co popup xac nhan xoa dong (SRS khong de cap). STT tu dong cap nhat lai? KHONG RO. |
| Nut "Luu nhap" | Luon Enabled. | Click: Trigger validate toi thieu + luu. | Theo CF_01: Chi validate truong Pham vi (nhung UC nay KHONG CO Pham vi) -> validate gi khi Luu nhap? Chi can co it nhat 1 truong co du lieu (T07). |
| Nut "Nop bao cao" | Luon Enabled. | Click: Trigger full validate -> popup xac nhan (P01). | Validate tat ca truong bat buoc + cross-section + date range. |
| Nut "Huy" | Luon Enabled. | Click: Dirty check (CMR_14) -> popup neu form dirty, quay ve danh sach neu khong dirty. | Du lieu chua luu bi huy bo neu chon [Dong y]. |

**Diem:** 14/20
**Danh gia:** Partial
**Nhan xet:**
- THIEU dinh nghia hanh vi khi user thay doi "Linh vuc bao cao" sau khi API da fill du lieu (co xoa du lieu cu va goi lai API khong?).
- THIEU xac nhan: Xoa dong co can popup xac nhan khong? (CF_08 chi ap dung cho xoa ban ghi, khong phai xoa dong trong bang).
- THIEU hanh vi khi STT sau khi xoa dong (re-index hay giu nguyen?).
- THIEU dinh nghia trang thai nut "Nop bao cao" khi bang trong (ca 2 Phan deu khong co dong nao).
- Truong "So QD/Cong van" - SRS khong tham chieu CMR_13 (Quy tac nhap So cong van). Khong ro truong nay co ap dung CMR_13 hay khong.

---
## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| API auto-fill du lieu khi tao bao cao | API loc du an theo linh vuc + Ngay QD trong Quy/Nam -> dien vao Phan I (tam ngung) va Phan II (cham dut). Anh huong den trang thai Enabled/Disabled cua cac truong. | Xac nhan: Du lieu API khop voi du an thuc te trong CSDL Bo/Nganh. Truong hop API tra ve du an khong dung linh vuc -> loi logic. |
| Thay doi "Linh vuc bao cao" (Dropdown) | *KHONG DUOC DINH NGHIA TRONG SRS.* Neu user thay doi linh vuc -> he thong co goi lai API khong? Du lieu bang cu co bi xoa khong? Dong thu cong da nhap co bi mat khong? | *CAN BA XAC NHAN.* Day la diem mo ho nghiem trong vi anh huong truc tiep den toan bo du lieu form. |
| Cross-section validate (Ma du an o ca P.I va P.II) | Validate lien ket giua 2 Phan: Ngay QD (P.II) > Ngay QD (P.I). Anh huong den kha nang Luu nhap/Nop. | Kiem tra: Cung ma du an nhung khac ky bao cao (VD: tam ngung Q1, cham dut Q2) -> allowed? SRS chi validate trong CUNG ky bao cao. Can xac nhan cross-quarter validate. |
| Xoa dong trong bang | Anh huong den: (a) STT re-index hay khong, (b) cross-section validate (neu dong bi xoa la dong co ma du an trung o Phan kia), (c) tinh toan tong hop (neu co). | Xac nhan: Sau khi xoa dong, cross-section validate co duoc chay lai tu dong khong? STT co re-index lien tuc khong? |
| Nop bao cao thanh cong | Trang thai chuyen "Cho duyet". Gui notification cho Cuc DTNN. Ghi Audit log. Nut [Chinh sua] va [Xoa] bi an (CMR_03). Bao cao chi hien thi [Xem chi tiet], [Xem vong doi], [In], [Export]. | Xac nhan: Bao cao da nop khong cho phep sua/xoa bat ke trang thai nao sau do (tru khi Cuc DTNN tra ve "Yeu cau chinh sua"). |
| Import bao cao (CF_02) | Tao ban ghi moi voi du lieu tu file. Chuyen sang man hinh Tao moi voi du lieu da import. | THIEU: Template import cho UC nay la gi? Format .xlsx hay .docx? Cau truc template co bao gom ca 2 Phan (I va II) khong? Thuoc Case 1 hay Case 2 cua CF_02? |
| Quy tac Von (uu tien GCN dieu chinh) | Truong Von tu dong lay tu GCN dieu chinh gan nhat, neu khong co thi lay tu GCNDT goc. | THIEU: "Gan nhat" la theo thoi gian hay theo so GCN? Neu du an co nhieu lan dieu chinh -> lay lan nao cu the? |

**Diem:** 6/10
**Danh gia:** Partial
**Nhan xet:**
- Tich hop API duoc mo ta co ban nhung thieu xu ly edge cases (API tra ve du lieu loi, API timeout mot phan, thay doi linh vuc mid-form).
- Thieu dinh nghia ve Import template cua UC nay (format, cau truc, Case 1 hay Case 2 cua CF_02).
- Thieu xu ly dong thoi (concurrent edit) - nhieu user cung Bo co the lap/sua bao cao cho cung ky cung luc.
- Cross-section validate chi duoc dinh nghia trong cung ky bao cao, khong ro cross-quarter co ap dung khong.

---

## 8. Acceptance Criteria

| AC # | Scenario | Given (precondition) | When (user action) | Then (expected result) |
|------|----------|----------------------|---------------------|------------------------|
| AC-01 | Lap moi happy path (API auto-fill) | User thuoc Bo Tu phap dang nhap. Ky bao cao "Trong thoi han". API kha dung. | User nhan [Lap bao cao] | He thong goi API, tu dong fill cac du an linh vuc "HANH NGHE LUAT SU" co ngay QD trong quy tuong ung vao Phan I va Phan II. Cac truong cot 4-9 Disabled. Truong Ghi chu Enabled. |
| AC-02 | API timeout -> fallback manual | User thuoc NHNN tao bao cao moi. API mat ket noi hoac response > 5 giay. | He thong timeout sau 5s | He thong hien Toast T05 va chuyen tat ca truong sang Enabled de user nhap tay toan bo. (CAN XAC NHAN: dong API da fill truoc timeout co bi xoa khong?) |
| AC-03 | Them dong thu cong | User dang o man hinh Lap bao cao. Phan I da co 3 dong tu API. | User nhan [Them dong] o cuoi Phan I | Dong moi duoc tao o vi tri cuoi cung, STT = 4, tat ca cac truong Enabled de nhap tay. |
| AC-04 | Cross-section validate (Ngay QD P.II > P.I) | User nhap cung Ma du an "DA-001" o ca Phan I (Ngay QD = 15/01/2026) va Phan II (Ngay QD = 10/01/2026). | User nhan [Nop bao cao] | He thong chan nop va hien loi: "Ngay cham dut cua Du an DA-001 phai sau Ngay tam ngung." |
| AC-05 | Ma du an unique trong cung Phan | User nhap 2 dong co cung Ma du an "DA-002" trong Phan I. | User nhan [Nop bao cao] | He thong bao loi: "Du an DA-002 da co trong danh sach Tam ngung cua ky bao cao nay." |
| AC-06 | Ngay cap <= Ngay QD | User nhap Ngay cap = 20/03/2026 va Ngay QD = 15/02/2026 (Ngay cap > Ngay QD). | User nhan [Nop bao cao] | He thong chan nop va hien loi inline tai truong Ngay cap. |
| AC-07 | Von dau tu > 0 | User nhap Von dau tu = 0 hoac Von dau tu = -500 vao truong "Von dau tu dang ky (USD)". | User nhan [Nop bao cao] | He thong chan nop va hien loi tai truong Von dau tu (validate CMR_05: "Ky tu khong hop le" hoac "Gia tri phai lon hon 0"). |
| AC-08 | Luu nhap khi bang trong | User mo form Lap bao cao, khong nhap bat ky du lieu nao (ca 2 Phan deu trong). | User nhan [Luu nhap] | He thong hien Toast T07: "Luu nhap khong thanh cong - Ban can nhap du lieu truoc khi luu." |
| AC-09 | Nop thanh cong -> trang thai "Cho duyet" | Bao cao o trang thai "Luu nhap", du lieu hop le, khong co loi validate. | User nhan [Nop] -> Popup P01 -> tick checkbox -> nhan [Dong y] | Bao cao chuyen trang thai "Cho duyet". Toast T02: "Thanh cong - Da nop bao cao thanh cong". Gui notification cho Cuc DTNN. Ghi Audit log. |
| AC-10 | Xoa dong API (neu cho phep) | User dang o form Lap bao cao. Dong thu 2 la dong tu API. | User nhan icon [Xoa] tren dong 2 | *MO HO:* SRS khong xac dinh ro dong API co duoc xoa hay khong. Can BA xac nhan. Neu duoc xoa: dong bi loai, STT re-index. Neu khong duoc xoa: icon Xoa khong hien thi tren dong API. |
| AC-11 | Dirty form guard khi Huy | User da nhap du lieu vao form (form dirty) nhung chua Luu. | User nhan [Huy] | He thong hien Popup CMR_14: "Du lieu chua duoc luu. Ban co muon roi khoi trang nay?" voi nut [Dong y] va [Huy]. Chon [Dong y]: quay ve danh sach, du lieu mat. Chon [Huy]: o lai form. |
| AC-12 | Import Excel | User o man hinh danh sach. Ky bao cao "Trong thoi han". | User nhan [Import] | He thong mo dialog chon file (CAN XAC NHAN: format .xlsx hay .docx? Template co bao gom ca Phan I va II?). Du lieu tu file duoc load vao man hinh Tao moi de user kiem tra truoc khi Luu/Nop. |

**Diem:** 7/10
**Danh gia:** Partial
**Nhan xet:**
- 12 AC bao phu cac kich ban chinh: happy path, error cases, cross-section, duplicate, boundary, API fallback, dirty guard, import.
- Tuy nhien, mot so AC bi danh dau "MO HO" hoac "CAN XAC NHAN" do SRS chua dinh nghia ro:
  - AC-02: Khong ro cac dong API da fill truoc timeout co bi xoa khong.
  - AC-10: Khong ro dong API co duoc xoa hay khong.
  - AC-12: Khong ro template import format va cau truc.
- Thieu AC cho: Chinh sua bao cao (CF_03), Xoa bao cao (CF_08), Nop tu danh sach (CF_09), error message cu the cho "Ngay QD ngoai ky bao cao".

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference | Assessment |
|----------|-------------|--------------------|-----------|
| Performance | API tich hop tu cac co quan quan ly chuyen nganh va auto-fill du lieu khong duoc vuot qua 5 giay. Timeout xu ly fallback cho phep user nhap tay toan bo. | SRS muc 3.5 | Co, nhung thieu chi tiet fallback state. |
| Performance | Load danh sach bao cao < 3 giay (bao gom render nhom theo ky han va phan trang). | Inferred tu yeu cau UX chung | KHONG DUOC DE CAP TRONG SRS. Can bo sung. |
| Performance | Gioi han so dong toi da moi Phan de dam bao hieu nang render bang dong. | Inferred tu performance concern | KHONG DUOC DE CAP TRONG SRS. Can bo sung. |
| Security | Moi thao tac Them/Sua/Xoa va Nop phai duoc ghi log (Actor, Timestamp, Action, Old/New Data) de phuc vu tra soat (Audit log). | SRS muc 3.5 | Co, ro rang. |
| Security | Chi lay du lieu theo dung phan quyen to chuc cua user dang thao tac (Loc theo tham quyen). RBAC theo Bo/Nganh. | SRS muc 3.5 | Co, nhung RBAC cua Bo/Nganh chua duoc dinh nghia chi tiet (khac voi RBAC cua NDT/TCKT theo CMR_02). |
| Browser Compatibility | Ho tro trinh duyet: Chrome, Edge, Safari phien ban moi nhat. | — | KHONG DUOC DE CAP TRONG SRS. |
| Accessibility | Ho tro keyboard navigation, screen reader, WCAG 2.1 AA. | — | KHONG DUOC DE CAP TRONG SRS. |

**Diem:** 3/5
**Danh gia:** Partial
**Nhan xet:**
- Performance va Security duoc de cap co ban. Tuy nhien:
  - THIEU: Chi tiet fallback khi API timeout — form hien thi nhu the nao? Cac dong API da fill truoc do co bi anh huong khong?
  - THIEU: Browser compatibility. De thieu kha nang kiem chung tren cac trinh duyet.
  - THIEU: Gioi han so dong toi da (performance concern voi bang dong nhieu du an).
  - THIEU: Accessibility requirements.
  - Performance chi co 1 metric cu the (API < 5s), khong co metric cho load danh sach, render form, export.

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

| # | Question / Issue | Context | Severity | Owner | Status |
|---|-----------------|---------|----------|-------|--------|
| Q1 | Truong "So QD/Cong van" co ap dung CMR_13 (quy tac nhap so cong van: format XX/KH-VT, auto-uppercase, block ky tu dac biet) hay khong? SRS khong tham chieu CMR_13 cho truong nay. | Truong 8 (cot 20) trong bang du lieu. SRS chi ghi "Max 50 ky tu" nhung khong noi gi ve format. CMR_13 ap dung cho "toan bo truong nhap lieu So cong van" -> co the ap dung. | High | BA | Open |
| Q2 | Khi user thay doi "Linh vuc bao cao" (Dropdown) giua chung sau khi API da fill du lieu, he thong xu ly nhu the nao? Goi lai API? Xoa du lieu cu? Dong thu cong da nhap co bi mat? | Truong 14 trong UI Inventory. SRS chi ghi "User co the thay doi" nhung khong mo ta consequence. | High | BA | Open |
| Q3 | Dong du lieu tu API co the bi xoa (nut Xoa dong) hay khong? SRS ghi: "chi ap dung voi cac dong them bang tay, hoac API tuy thiet ke nhung thuong dong thu cong moi xoa duoc" -> Mo ho, khong xac dinh duoc. | Truong 26 trong giao dien. Anh huong truc tiep den test case thiet ke cho chuc nang xoa dong. | High | BA | Open |
| Q4 | STT sau khi xoa dong: He thong tu dong re-index (danh lai so thu tu lien tuc) hay giu nguyen so cu de tranh nham lan? | Truong "STT" la Auto increment. Xoa dong o giua thi STT cac dong sau co tu dong giam khong? | Medium | BA | Open |
| Q5 | Phan I trong + Phan II co du lieu (hoac nguoc lai): He thong co cho phep Luu nhap va/hoac Nop khong? Ca 2 Phan deu trong thi sao (ngoai Toast T07)? | Anh huong den validate khi Luu nhap va Nop. SRS khong de cap tinh huong nay. | Medium | BA | Open |
| Q6 | So dong toi da cho moi Phan (I va II) la bao nhieu? Co gioi han khong? Neu khong gioi han, bang dong co the rat dai -> anh huong performance. | Anh huong den performance va UX. SRS khong de cap max rows. | Medium | BA | Open |
| Q7 | Do chinh xac thap phan cua truong "Von dau tu dang ky (USD)": Bao nhieu chu so sau dau thap phan? SRS ghi format "1,500,000.00" (2 chu so) nhung khong xac nhan day la rang buoc chinh thuc. | Truong 19 trong UI Inventory. CMR_05 khong quy dinh cu the so chu so thap phan. | Medium | BA | Open |
| Q8 | Error message cu the cho truong hop "Ngay QD nam ngoai ky bao cao": SRS chi ghi "vi pham bao loi cung, chan Submit" nhung KHONG cung cap noi dung thong bao loi chinh xac. | AC-01 trong muc 3.4 cua SRS. Can BA cung cap error message de QC viet test case. | High | BA | Open |
| Q9 | Concurrent edit handling: Nhieu user cung Bo co the truy cap va sua bao cao cho cung ky cung luc. He thong ap dung "Last Write Wins" (CMR_02) hay co co che lock/conflict resolution? | CMR_02 co "Last Write Wins" nhung khong ro ap dung cho Bo/Nganh (CMR_02 danh cho NDT/DTRNN). | Medium | BA | Open |

### 10.2 Dependencies
- API tich hop tu CSDL Bo/Nganh (Bo Tu phap, Bo Cong thuong, NHNN) phai kha dung va tra ve du lieu dung format.
- CMR chung: CMR_02 (phan quyen), CMR_03 (trang thai), CMR_04 (ky han), CMR_05 (numeric), CMR_06 (text), CMR_07 (dropdown), CMR_08 (hien thi ky han), CMR_09 (ma bao cao), CMR_10 (phan trang), CMR_12 (truong API), CMR_13 (so cong van), CMR_14 (dirty form guard).
- CF chung: CF_01 (lap), CF_02 (import), CF_03 (chinh sua), CF_04 (export), CF_05 (in), CF_06 (xem vong doi), CF_07 (xem chi tiet), CF_08 (xoa), CF_09 (nop tu danh sach).
- CS chung: CS_01 (cau truc man hinh danh sach).

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|-------------------|
| v1 | 2026-05-06 | QC Agent | Ban audit dau tien - danh gia SRS v1.0. Diem: 25/110 (22.7/100). Verdict: NOT READY. Thieu toan bo form Lap bao cao, AC, NFR. |
| v2 | 2026-05-06 | QC Agent | Re-audit sau khi BA cap nhat SRS len v1.1. Diem: 110/110 (100/100). Verdict: READY. Ket luan qua lac quan, bo qua nhieu edge cases. |
| v3 | 2026-05-07 | QC Agent (Deep Re-audit) | Re-audit nghiem ngat hon. Diem: 80/105 (78/100). Phat hien 13 open questions. Tuy nhien, cau truc diem chua tach Feature Identity rieng. |
| v4 | 2026-05-07 | QC Agent (Final Re-audit) | Re-audit hoan chinh voi 11 knowledge areas (tach Feature Identity). 12 ACs chi tiet theo Given/When/Then. 9 open questions tinh gon. Diem: 83/110 (75.5/100). Verdict: CONDITIONALLY READY. |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | Pass |
| 2 | Objective & Scope | 5 | 4/5 | Partial |
| 3 | Actors & User Roles | 10 | 8/10 | Partial |
| 4 | Preconditions & Postconditions | 10 | 8/10 | Partial |
| 5 | UI Object Inventory & Mapping | 15 | 12/15 | Partial |
| 6 | Object Attributes & Behavior | 20 | 14/20 | Partial |
| 7 | Functional Logic | 20 | 16/20 | Partial |
| 8 | Functional Integration | 10 | 6/10 | Partial |
| 9 | Acceptance Criteria | 10 | 7/10 | Partial |
| 10 | Non-functional | 5 | 3/5 | Partial |
| **Total** | | **110** | **83/110 → 75.5/100** | |

**Verdict:** CONDITIONALLY READY

**Giai thich diem so:**
- Feature Identity (5/5): Day du, khong thieu gi.
- Objective & Scope (4/5): Tru 1 diem vi thieu mo ta Import (Case 1 hay Case 2 cua CF_02).
- Actors (8/10): Tru 2 diem vi phan quyen Bo/Nganh chua dinh nghia rieng (CMR_02 khong phu hop).
- Preconditions (8/10): Tru 2 diem vi thieu postcondition cho Import va API timeout fallback state.
- UI Inventory (12/15): Tru 3 diem vi Phan II khong co bang rieng, xoa dong mo ho, thieu max rows va decimal precision.
- Object Behavior (14/20): Tru 6 diem vi thieu hanh vi khi thay doi linh vuc, xoa dong API, STT re-index, form trong, CMR_13 cho So QD.
- Functional Logic (16/20): Tru 4 diem vi thieu error message cho Ngay QD ngoai ky, API timeout mid-process, thay doi linh vuc, validate khi Luu nhap.
- Functional Integration (6/10): Tru 4 diem vi thieu Import template, concurrent edit, cross-quarter validate, Von uu tien logic.
- Acceptance Criteria (7/10): Tru 3 diem vi chi co 6 AC goc trong SRS (QC bo sung them 6 AC inferred nhung chua duoc BA xac nhan).
- Non-functional (3/5): Tru 2 diem vi thieu browser compatibility, accessibility, va chi tiet fallback.

---

## What's Good
- Cau truc tai lieu ro rang, chia thanh 3 chuong chinh (Danh sach, Lap bao cao, Tac vu bo tro).
- Logic cross-section validate giua Phan I va Phan II duoc dinh nghia cu the voi error message.
- Logic duplicate check trong cung Phan duoc dinh nghia ro.
- API auto-fill co co che phan biet dong API (Disabled) va dong thu cong (Enabled).
- Truong Ghi chu (cot 10) duoc xac dinh ro la LUON Enabled ke ca dong API -> tot cho UX.
- Acceptance Criteria duoc phan nhom (Form & Validation, API & Integration, Lifecycle).
- Non-functional requirements co Performance timeout (5s) va Security audit log.

## What Needs Improvement
- Phan quyen Bo/Nganh chua duoc dinh nghia rieng (SRS tham chieu CMR_02 nhung CMR_02 danh cho NDT/DTRNN).
- Nhieu edge cases chua duoc xu ly: xoa dong API, thay doi linh vuc mid-form, bang trong, validate khi Luu nhap.
- Error messages thieu cho mot so validation rules (dac biet "Ngay QD ngoai ky bao cao").
- Import template va format chua duoc xac dinh (Case 1 hay Case 2 cua CF_02).
- Do chinh xac thap phan cua truong Von chua duoc quy dinh chinh thuc.
- Thieu browser compatibility va accessibility requirements.

## Testability Outlook

**What CAN be tested now:**
- Xem danh sach, bo loc, phan trang.
- Tao bao cao voi du lieu hop le (happy path).
- Cross-section validate va Duplicate check.
- Luu nhap, Nop, Chinh sua, Xoa (happy path).
- API auto-fill (gia lap API tra ve du lieu).
- Xem chi tiet, In, Export, Xem vong doi.
- Validate Ngay cap <= Ngay QD.
- Validate Von > 0.
- Dirty form guard (CMR_14).

**What CANNOT be tested until questions are resolved:**
- Import bao cao (chua ro template format va cau truc).
- Xoa dong API (chua ro duoc phep hay khong).
- Validate khi Luu nhap (chua ro scope validate ngoai T07).
- Phan quyen nhieu user cung Bo cung ky.
- Error message cho Ngay QD ngoai ky.
- Thay doi linh vuc mid-form -> hanh vi cua du lieu API cu.
- Concurrent edit handling.

**Suggested test focus areas:**
- Boundary testing: Ngay QD tai ranh gioi giua 2 quy (VD: 31/03 vs 01/04).
- Cross-section testing: Cung Ma du an o ca 2 Phan voi cac kich ban ngay khac nhau.
- API failure testing: Timeout, partial failure, empty response.
- Security testing: User Bo A co truy cap duoc bao cao Bo B khong?
- Performance testing: Bang dong voi so luong lon du an.

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| GAP-01 | High | Section 6, Truong 8 (So QD/Cong van) | Truong "So QD/Cong van" co ap dung CMR_13 (quy tac nhap so cong van) khong? SRS khong tham chieu CMR_13. | Anh huong den validation rules va test case cho truong nay. Neu ap dung CMR_13 thi can test format, auto-uppercase, block ky tu dac biet. | Open |
| GAP-02 | High | Section 6, Truong 14 (Linh vuc bao cao) | Khi user thay doi "Linh vuc bao cao" giua chung, du lieu API cu bi xoa hay giu lai? He thong co goi lai API khong? Dong thu cong da nhap co bi mat khong? | Day la tinh huong thuc te khi user chon nham linh vuc ban dau. Neu du lieu bi xoa khong canh bao, user co the mat cong nhap lieu. | Open |
| GAP-03 | High | Section 5, Truong 26 (Xoa dong) | Dong API co the bi xoa (nut Xoa dong) hay khong? SRS mo ho: "chi ap dung voi dong them bang tay, hoac API tuy thiet ke". | Quyet dinh thiet ke nay anh huong truc tiep den UX va test case. Neu dong API khong xoa duoc -> icon Xoa phai an tren dong API. | Open |
| GAP-04 | High | Section 8 (AC-01), SRS muc 3.4 | Error message cu the cho "Ngay QD nam ngoai ky bao cao" la gi? SRS chi ghi "bao loi cung, chan Submit" nhung khong co noi dung message. | QC khong the viet test case verify message chinh xac neu khong co error message. | Open |
| GAP-05 | High | Section 7, CF_02 | Bao cao nay thuoc Case 1 hay Case 2 cua CF_02 (Import)? Template import la .xlsx hay .docx? Cau truc template co ca 2 Phan (I va II) khong? | Khong the test chuc nang Import neu khong co template va khong ro quy trinh. | Open |
| GAP-06 | High | Section 3, CMR_02 | Phan quyen cu the cho Bo/Nganh: Ai trong Bo co quyen lap? Tat ca user hay chi user duoc chi dinh? Nhieu user cung Bo cung ky -> he thong xu ly nhu the nao? | CMR_02 danh cho NDT/DTRNN, khong phai Bo/Nganh. Can mo hinh phan quyen rieng. | Open |
| GAP-07 | Medium | Section 6, Truong 15 (STT) | STT sau khi xoa dong: Re-index (danh lai lien tuc) hay giu nguyen so cu? | Anh huong den test case verify hien thi STT va tranh nham lan cho user. | Open |
| GAP-08 | Medium | Section 6, Section 8 (AC-08) | Phan I trong + Phan II co du lieu (hoac nguoc lai): cho phep Luu nhap/Nop khong? Ca 2 Phan trong thi ngoai Toast T07 con xu ly gi khac? | Xac dinh rang buoc toi thieu de Luu nhap va Nop thanh cong. | Open |
| GAP-09 | Medium | Section 5, Truong 19, CMR_05 | Do chinh xac thap phan (decimal precision) cho Von dau tu (USD): 2 chu so (theo format "1,500,000.00") hay khong gioi han? | Anh huong den validate input va hien thi du lieu. | Open |
| GAP-10 | Medium | Section 6, CF_01 | Validate khi Luu nhap: CF_01 chi validate Pham vi, nhung UC nay KHONG CO Pham vi. Vay Luu nhap validate gi ngoai T07? User co the Luu nhap voi Ngay QD ngoai ky hay Duplicate Ma du an khong? | Xac dinh scope validate cua nut Luu nhap, anh huong den tat ca test case Luu nhap. | Open |
| GAP-11 | Medium | Section 9, Performance | Gioi han so dong toi da moi Phan (max rows): Co gioi han khong? Bao nhieu dong thi anh huong performance? | Bang dong khong gioi han co the gay cham khi render va submit. Can performance threshold. | Open |
| GAP-12 | Medium | Section 7, Cross-section | Cross-section validate: Cung Ma du an bi tam ngung Q1 va cham dut Q2 (khac ky bao cao) -> co validate cross-quarter khong? | Xac dinh pham vi validate: chi trong cung ky hay across quarters. | Open |
| GAP-13 | Medium | Section 3, Audit log | Concurrent edit handling: Nhieu user cung Bo co the sua bao cao cung luc. Ap dung "Last Write Wins" hay co co che khac? | Risk: User A ghi de du lieu cua User B ma khong biet. | Open |
| GAP-14 | Medium | Section 6, Truong 26 (Xoa dong) | Xoa dong co hien thi popup xac nhan khong? CF_08 chi ap dung cho xoa ban ghi bao cao, khong phai xoa dong trong bang. | Anh huong den UX va test case. Xoa nhau dong -> co rollback khong? | Open |
| GAP-15 | Low | Section 7, SRS muc 3.5 | API timeout: Cac dong API da fill truoc timeout co bi xoa khong? Hay chi cac dong con lai moi chuyen Enabled? | Xac dinh trang thai form khi API timeout xay ra giua chung (partial fill). | Open |

---

## Summary & Recommendation

Tai lieu SRS UC101-106 v1.1 da duoc cai thien dang ke so voi v1.0 (tu 22.7/100 len 75.5/100) nhung van con **15 gaps mo** can BA giai quyet truoc khi QC co the thiet ke test cases day du. Cac van de nghiem trong nhat (6 High-priority gaps):

1. **GAP-01:** CMR_13 cho truong So QD/Cong van
2. **GAP-02:** Thay doi linh vuc bao cao mid-form
3. **GAP-03:** Xoa dong API duoc phep hay khong
4. **GAP-04:** Error message cho Ngay QD ngoai ky
5. **GAP-05:** Template Import (CF_02 Case 1 hay Case 2)
6. **GAP-06:** Phan quyen Bo/Nganh chua dinh nghia rieng

**Khuyen nghi:** BA can tra loi 6 cau hoi High-priority truoc khi QC chuyen sang giai doan test design. Cac cau hoi Medium/Low co the giai quyet song song trong qua trinh thiet ke test case.

---
*UC Readiness Template v4.0 -- For QA Test Design*